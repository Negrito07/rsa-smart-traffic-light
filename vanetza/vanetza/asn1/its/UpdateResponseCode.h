/*
 * Generated by asn1c-0.9.29 (http://lionet.info/asn1c)
 * From ASN.1 module "EV-RechargingSpotReservation-PDU-Descriptions"
 * 	found in "/home/rrosmaninho/vanetza/asn1/EV-RSR-PDU-Descriptions.asn"
 * 	`asn1c -fcompound-names -fincludes-quoted -no-gen-example -R -D /home/rrosmaninho/vanetza/vanetza/asn1/its`
 */

#ifndef	_UpdateResponseCode_H_
#define	_UpdateResponseCode_H_


#include "asn_application.h"

/* Including external dependencies */
#include "NativeEnumerated.h"

#ifdef __cplusplus
extern "C" {
#endif

/* Dependencies */
typedef enum UpdateResponseCode {
	UpdateResponseCode_ok	= 0,
	UpdateResponseCode_unknown_Reservation_ID	= 1,
	UpdateResponseCode_mismatching_Reservation_Password	= 2,
	UpdateResponseCode_invalid_Arrival_Time	= 3,
	UpdateResponseCode_invalid_Departure_Time	= 4
} e_UpdateResponseCode;

/* UpdateResponseCode */
typedef long	 UpdateResponseCode_t;

/* Implementation */
extern asn_per_constraints_t asn_PER_type_UpdateResponseCode_constr_1;
extern asn_TYPE_descriptor_t asn_DEF_UpdateResponseCode;
extern const asn_INTEGER_specifics_t asn_SPC_UpdateResponseCode_specs_1;
asn_struct_free_f UpdateResponseCode_free;
asn_struct_print_f UpdateResponseCode_print;
asn_constr_check_f UpdateResponseCode_constraint;
ber_type_decoder_f UpdateResponseCode_decode_ber;
der_type_encoder_f UpdateResponseCode_encode_der;
xer_type_decoder_f UpdateResponseCode_decode_xer;
xer_type_encoder_f UpdateResponseCode_encode_xer;
oer_type_decoder_f UpdateResponseCode_decode_oer;
oer_type_encoder_f UpdateResponseCode_encode_oer;
per_type_decoder_f UpdateResponseCode_decode_uper;
per_type_encoder_f UpdateResponseCode_encode_uper;
per_type_decoder_f UpdateResponseCode_decode_aper;
per_type_encoder_f UpdateResponseCode_encode_aper;

#ifdef __cplusplus
}
#endif

#endif	/* _UpdateResponseCode_H_ */
#include "asn_internal.h"
