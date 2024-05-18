/*
 * Generated by asn1c-0.9.29 (http://lionet.info/asn1c)
 * From ASN.1 module "TIS-TPG-Transactions-Descriptions"
 * 	found in "asn1/TIS-TPG-Transactions-Descriptions.asn"
 * 	`asn1c -fcompound-names -fincludes-quoted -no-gen-example -R`
 */

#ifndef	_PressureVariantsList_H_
#define	_PressureVariantsList_H_


#include "asn_application.h"

/* Including external dependencies */
#include "asn_SEQUENCE_OF.h"
#include "constr_SEQUENCE_OF.h"

#ifdef __cplusplus
extern "C" {
#endif

/* Forward declarations */
struct PressureVariant;

/* PressureVariantsList */
typedef struct PressureVariantsList {
	A_SEQUENCE_OF(struct PressureVariant) list;
	
	/* Context for parsing across buffer boundaries */
	asn_struct_ctx_t _asn_ctx;
} PressureVariantsList_t;

/* Implementation */
extern asn_TYPE_descriptor_t asn_DEF_PressureVariantsList;
extern asn_SET_OF_specifics_t asn_SPC_PressureVariantsList_specs_1;
extern asn_TYPE_member_t asn_MBR_PressureVariantsList_1[1];
extern asn_per_constraints_t asn_PER_type_PressureVariantsList_constr_1;

#ifdef __cplusplus
}
#endif

/* Referred external types */
#include "PressureVariant.h"

#endif	/* _PressureVariantsList_H_ */
#include "asn_internal.h"
