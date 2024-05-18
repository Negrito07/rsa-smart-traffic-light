/*
 * Generated by asn1c-0.9.29 (http://lionet.info/asn1c)
 * From ASN.1 module "EfcDsrcApplication"
 * 	found in "build.asn1/iso/ISO14906-0-6.asn"
 * 	`asn1c -fcompound-names -fincludes-quoted -no-gen-example -R`
 */

#include "EuroValue.h"

/*
 * This type is implemented using NativeEnumerated,
 * so here we adjust the DEF accordingly.
 */
#if !defined(ASN_DISABLE_OER_SUPPORT)
static asn_oer_constraints_t asn_OER_type_EuroValue_constr_1 CC_NOTUSED = {
	{ 0, 0 },
	-1};
#endif  /* !defined(ASN_DISABLE_OER_SUPPORT) */
#if !defined(ASN_DISABLE_UPER_SUPPORT) || !defined(ASN_DISABLE_APER_SUPPORT)
asn_per_constraints_t asn_PER_type_EuroValue_constr_1 CC_NOTUSED = {
	{ APC_CONSTRAINED,	 4,  4,  0,  15 }	/* (0..15) */,
	{ APC_UNCONSTRAINED,	-1, -1,  0,  0 },
	0, 0	/* No PER value map */
};
#endif  /* !defined(ASN_DISABLE_UPER_SUPPORT) || !defined(ASN_DISABLE_APER_SUPPORT) */
static const asn_INTEGER_enum_map_t asn_MAP_EuroValue_value2enum_1[] = {
	{ 0,	7,	"noEntry" },
	{ 1,	6,	"euro-1" },
	{ 2,	6,	"euro-2" },
	{ 3,	6,	"euro-3" },
	{ 4,	6,	"euro-4" },
	{ 5,	6,	"euro-5" },
	{ 6,	6,	"euro-6" },
	{ 7,	15,	"reservedForUse1" },
	{ 8,	15,	"reservedForUse2" },
	{ 9,	15,	"reservedForUse3" },
	{ 10,	15,	"reservedForUse4" },
	{ 11,	15,	"reservedForUse5" },
	{ 12,	15,	"reservedForUse6" },
	{ 13,	15,	"reservedForUse7" },
	{ 14,	15,	"reservedForUse8" },
	{ 15,	3,	"eev" }
};
static const unsigned int asn_MAP_EuroValue_enum2value_1[] = {
	15,	/* eev(15) */
	1,	/* euro-1(1) */
	2,	/* euro-2(2) */
	3,	/* euro-3(3) */
	4,	/* euro-4(4) */
	5,	/* euro-5(5) */
	6,	/* euro-6(6) */
	0,	/* noEntry(0) */
	7,	/* reservedForUse1(7) */
	8,	/* reservedForUse2(8) */
	9,	/* reservedForUse3(9) */
	10,	/* reservedForUse4(10) */
	11,	/* reservedForUse5(11) */
	12,	/* reservedForUse6(12) */
	13,	/* reservedForUse7(13) */
	14	/* reservedForUse8(14) */
};
const asn_INTEGER_specifics_t asn_SPC_EuroValue_specs_1 = {
	asn_MAP_EuroValue_value2enum_1,	/* "tag" => N; sorted by tag */
	asn_MAP_EuroValue_enum2value_1,	/* N => "tag"; sorted by N */
	16,	/* Number of elements in the maps */
	0,	/* Enumeration is not extensible */
	1,	/* Strict enumeration */
	0,	/* Native long size */
	0
};
static const ber_tlv_tag_t asn_DEF_EuroValue_tags_1[] = {
	(ASN_TAG_CLASS_UNIVERSAL | (10 << 2))
};
asn_TYPE_descriptor_t asn_DEF_EuroValue = {
	"EuroValue",
	"EuroValue",
	&asn_OP_NativeEnumerated,
	asn_DEF_EuroValue_tags_1,
	sizeof(asn_DEF_EuroValue_tags_1)
		/sizeof(asn_DEF_EuroValue_tags_1[0]), /* 1 */
	asn_DEF_EuroValue_tags_1,	/* Same as above */
	sizeof(asn_DEF_EuroValue_tags_1)
		/sizeof(asn_DEF_EuroValue_tags_1[0]), /* 1 */
	{
#if !defined(ASN_DISABLE_OER_SUPPORT)
		&asn_OER_type_EuroValue_constr_1,
#endif  /* !defined(ASN_DISABLE_OER_SUPPORT) */
#if !defined(ASN_DISABLE_UPER_SUPPORT) || !defined(ASN_DISABLE_APER_SUPPORT)
		&asn_PER_type_EuroValue_constr_1,
#endif  /* !defined(ASN_DISABLE_UPER_SUPPORT) || !defined(ASN_DISABLE_APER_SUPPORT) */
		NativeEnumerated_constraint
	},
	0, 0,	/* Defined elsewhere */
	&asn_SPC_EuroValue_specs_1	/* Additional specs */
};

