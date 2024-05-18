/*
 * Generated by asn1c-0.9.29 (http://lionet.info/asn1c)
 * From ASN.1 module "MCM-PDU-Descriptions"
 * 	found in "asn1/MCM-PDU-Descriptions.asn"
 * 	`asn1c -fcompound-names -fincludes-quoted -no-gen-example -R`
 */

#ifndef	_VehicleAutomationState_H_
#define	_VehicleAutomationState_H_


#include "asn_application.h"

/* Including external dependencies */
#include "BOOLEAN.h"
#include "constr_SEQUENCE.h"

#ifdef __cplusplus
extern "C" {
#endif

/* VehicleAutomationState */
typedef struct VehicleAutomationState {
	BOOLEAN_t	 humanDrivingLongitudinalAutomated;
	BOOLEAN_t	 humanDrivenLateralAutomated;
	BOOLEAN_t	 automatedDriving;
	
	/* Context for parsing across buffer boundaries */
	asn_struct_ctx_t _asn_ctx;
} VehicleAutomationState_t;

/* Implementation */
extern asn_TYPE_descriptor_t asn_DEF_VehicleAutomationState;
extern asn_SEQUENCE_specifics_t asn_SPC_VehicleAutomationState_specs_1;
extern asn_TYPE_member_t asn_MBR_VehicleAutomationState_1[3];

#ifdef __cplusplus
}
#endif

#endif	/* _VehicleAutomationState_H_ */
#include "asn_internal.h"
