/*
 * Generated by asn1c-0.9.29 (http://lionet.info/asn1c)
 * From ASN.1 module "MCM-PDU-Descriptions"
 * 	found in "asn1/MCM-PDU-Descriptions.asn"
 * 	`asn1c -fcompound-names -fincludes-quoted -no-gen-example -R`
 */

#ifndef	_ManouevreResponse_H_
#define	_ManouevreResponse_H_


#include "asn_application.h"

/* Including external dependencies */
#include "BOOLEAN.h"
#include "NativeEnumerated.h"
#include "constr_CHOICE.h"

#ifdef __cplusplus
extern "C" {
#endif

/* Dependencies */
typedef enum ManouevreResponse_PR {
	ManouevreResponse_PR_NOTHING,	/* No components present */
	ManouevreResponse_PR_offerAcceptation,
	ManouevreResponse_PR_offerDecline,
	ManouevreResponse_PR_requestAcceptation,
	ManouevreResponse_PR_requestDecline
} ManouevreResponse_PR;
typedef enum ManouevreResponse__requestDecline {
	ManouevreResponse__requestDecline_agreementSeekingUnknown	= 0,
	ManouevreResponse__requestDecline_agreementSeekingUnwanted	= 2,
	ManouevreResponse__requestDecline_allUnableToConform	= 1,
	ManouevreResponse__requestDecline_allUnableToUnderstand	= 3,
	ManouevreResponse__requestDecline_allErroneousBehaviourDetected	= 4,
	ManouevreResponse__requestDecline_allMissbehaviourDetected	= 5
} e_ManouevreResponse__requestDecline;

/* ManouevreResponse */
typedef struct ManouevreResponse {
	ManouevreResponse_PR present;
	union ManouevreResponse_u {
		BOOLEAN_t	 offerAcceptation;
		BOOLEAN_t	 offerDecline;
		BOOLEAN_t	 requestAcceptation;
		long	 requestDecline;
	} choice;
	
	/* Context for parsing across buffer boundaries */
	asn_struct_ctx_t _asn_ctx;
} ManouevreResponse_t;

/* Implementation */
/* extern asn_TYPE_descriptor_t asn_DEF_requestDecline_5;	// (Use -fall-defs-global to expose) */
extern asn_TYPE_descriptor_t asn_DEF_ManouevreResponse;

#ifdef __cplusplus
}
#endif

#endif	/* _ManouevreResponse_H_ */
#include "asn_internal.h"