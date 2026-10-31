"""Test 2 logic: fundamentally different principles survive; cosmetic variants and same-solution pairs merge."""
from iie.invention.diversity import compare, diversity_report


def C(i, title, principle, how, pc, bm, mc="polymer", vt="convenience", im="passive_object"):
    return {"id": f"c{i}", "title": title, "principle": principle, "user_value": vt, "business_model": bm,
            "axes": {"principle_class": pc, "value_type": vt, "material_class": mc, "business_model_class": bm,
                     "interaction_mode": im}, "detail": {"how_it_works": how, "materials": [mc]}}


DISTINCT = [
    C(1, "Evaporative clay cooler", "Water evaporating through porous terracotta absorbs heat from stored food",
      "Unglazed clay walls stay wet; evaporation lowers the inner temperature without power", "thermal", "product_sale", "ceramic_glass"),
    C(2, "Shared cold room by the hour", "Village cooperative rents insulated solar-powered cold storage capacity per crate",
      "Farmers book crates through a phone line and pay per day of storage", "logistical", "rental_access", "mixed",
      im="service_delivered"),
    C(3, "Edible coating licence", "Plant-based lipid coating slows moisture loss and ripening on fruit skins",
      "Fruit is dipped in a thin emulsion at the farm gate before transport", "chemical", "licensing_royalty", "bio_based",
      im="consumable"),
]


def test_three_different_principles_form_three_families():
    rep = diversity_report(DISTINCT)
    assert rep["family_count"] == 3 and rep["meets_requirement"]
    assert len(rep["distinct_principle_classes"]) == 3


def test_cosmetic_variants_are_merged():
    a = DISTINCT[0]
    b = C(9, "Evaporative clay cooler in matte red", a["principle"], a["detail"]["how_it_works"] + " Larger glossy finish.",
          "thermal", "product_sale", "ceramic_glass")
    pairs = compare([a, b])
    assert pairs[0]["verdict"] in ("cosmetic_variant", "same_solution")
    rep = diversity_report([a, b, DISTINCT[1]])
    assert rep["family_count"] == 2 and not rep["meets_requirement"]


def test_same_solution_with_different_name_is_merged():
    a = DISTINCT[0]
    b = C(8, "TerraChill pot", "Porous terracotta pot cools stored vegetables as water evaporates through its walls",
          "Keep the clay walls wet so evaporation lowers the inside temperature without electricity", "thermal",
          "product_sale", "ceramic_glass")
    pairs = compare([a, b])
    assert pairs[0]["verdict"] in ("same_solution", "cosmetic_variant"), pairs[0]
