/*
 * Generated by asn1c-0.9.29 (http://lionet.info/asn1c)
 * From ASN.1 module "AddGrpC"
 * 	found in "build.asn1/iso/ISO19091.asn"
 * 	`asn1c -fcompound-names -fincludes-quoted -no-gen-example -R`
 */

#include "ExceptionalCondition.h"

/*
 * This type is implemented using NativeEnumerated,
 * so here we adjust the DEF accordingly.
 */
#if !defined(ASN_DISABLE_OER_SUPPORT)
static asn_oer_constraints_t asn_OER_type_ExceptionalCondition_constr_1 CC_NOTUSED = {
	{ 0, 0 },
	-1};
#endif  /* !defined(ASN_DISABLE_OER_SUPPORT) */
#if !defined(ASN_DISABLE_UPER_SUPPORT) || !defined(ASN_DISABLE_APER_SUPPORT)
asn_per_constraints_t asn_PER_type_ExceptionalCondition_constr_1 CC_NOTUSED = {
	{ APC_CONSTRAINED | APC_EXTENSIBLE,  4,  4,  0,  12 }	/* (0..12,...) */,
	{ APC_UNCONSTRAINED,	-1, -1,  0,  0 },
	0, 0	/* No PER value map */
};
#endif  /* !defined(ASN_DISABLE_UPER_SUPPORT) || !defined(ASN_DISABLE_APER_SUPPORT) */
static const asn_INTEGER_enum_map_t asn_MAP_ExceptionalCondition_value2enum_1[] = {
	{ 0,	7,	"unknown" },
	{ 1,	23,	"publicTransportPriority" },
	{ 2,	24,	"emergencyVehiclePriority" },
	{ 3,	13,	"trainPriority" },
	{ 4,	10,	"bridgeOpen" },
	{ 5,	13,	"vehicleHeight" },
	{ 6,	7,	"weather" },
	{ 7,	10,	"trafficJam" },
	{ 8,	13,	"tunnelClosure" },
	{ 9,	14,	"meteringActive" },
	{ 10,	13,	"truckPriority" },
	{ 11,	22,	"bicyclePlatoonPriority" },
	{ 12,	22,	"vehiclePlatoonPriority" }
	/* This list is extensible */
};
static const unsigned int asn_MAP_ExceptionalCondition_enum2value_1[] = {
	11,	/* bicyclePlatoonPriority(11) */
	4,	/* bridgeOpen(4) */
	2,	/* emergencyVehiclePriority(2) */
	9,	/* meteringActive(9) */
	1,	/* publicTransportPriority(1) */
	7,	/* trafficJam(7) */
	3,	/* trainPriority(3) */
	10,	/* truckPriority(10) */
	8,	/* tunnelClosure(8) */
	0,	/* unknown(0) */
	5,	/* vehicleHeight(5) */
	12,	/* vehiclePlatoonPriority(12) */
	6	/* weather(6) */
	/* This list is extensible */
};
const asn_INTEGER_specifics_t asn_SPC_ExceptionalCondition_specs_1 = {
	asn_MAP_ExceptionalCondition_value2enum_1,	/* "tag" => N; sorted by tag */
	asn_MAP_ExceptionalCondition_enum2value_1,	/* N => "tag"; sorted by N */
	13,	/* Number of elements in the maps */
	14,	/* Extensions before this member */
	1,	/* Strict enumeration */
	0,	/* Native long size */
	0
};
static const ber_tlv_tag_t asn_DEF_ExceptionalCondition_tags_1[] = {
	(ASN_TAG_CLASS_UNIVERSAL | (10 << 2))
};
asn_TYPE_descriptor_t asn_DEF_ExceptionalCondition = {
	"ExceptionalCondition",
	"ExceptionalCondition",
	&asn_OP_NativeEnumerated,
	asn_DEF_ExceptionalCondition_tags_1,
	sizeof(asn_DEF_ExceptionalCondition_tags_1)
		/sizeof(asn_DEF_ExceptionalCondition_tags_1[0]), /* 1 */
	asn_DEF_ExceptionalCondition_tags_1,	/* Same as above */
	sizeof(asn_DEF_ExceptionalCondition_tags_1)
		/sizeof(asn_DEF_ExceptionalCondition_tags_1[0]), /* 1 */
	{
#if !defined(ASN_DISABLE_OER_SUPPORT)
		&asn_OER_type_ExceptionalCondition_constr_1,
#endif  /* !defined(ASN_DISABLE_OER_SUPPORT) */
#if !defined(ASN_DISABLE_UPER_SUPPORT) || !defined(ASN_DISABLE_APER_SUPPORT)
		&asn_PER_type_ExceptionalCondition_constr_1,
#endif  /* !defined(ASN_DISABLE_UPER_SUPPORT) || !defined(ASN_DISABLE_APER_SUPPORT) */
		NativeEnumerated_constraint
	},
	0, 0,	/* Defined elsewhere */
	&asn_SPC_ExceptionalCondition_specs_1	/* Additional specs */
};

