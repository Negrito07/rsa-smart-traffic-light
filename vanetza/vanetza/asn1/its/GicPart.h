/*
 * Generated by asn1c-0.9.29 (http://lionet.info/asn1c)
 * From ASN.1 module "IVI"
 * 	found in "build.asn1/iso/ISO19321.asn"
 * 	`asn1c -fcompound-names -fincludes-quoted -no-gen-example -R`
 */

#ifndef	_GicPart_H_
#define	_GicPart_H_


#include "asn_application.h"

/* Including external dependencies */
#include "Direction.h"
#include "NativeInteger.h"
#include "IviType.h"
#include "IviPurpose.h"
#include "LaneStatus.h"
#include "IVI_DriverCharacteristics.h"
#include "RoadSignCodes.h"
#include "constr_SEQUENCE.h"

#ifdef __cplusplus
extern "C" {
#endif

/* Forward declarations */
struct ZoneIds;
struct VarLengthNumber;
struct LanePositions;
struct VehicleCharacteristicsList;
struct ConstraintTextLines1;

/* GicPart */
typedef struct GicPart {
	struct ZoneIds	*detectionZoneIds;	/* OPTIONAL */
	struct VarLengthNumber	*its_Rrid;	/* OPTIONAL */
	struct ZoneIds	*relevanceZoneIds;	/* OPTIONAL */
	Direction_t	*direction;	/* OPTIONAL */
	struct ZoneIds	*driverAwarenessZoneIds;	/* OPTIONAL */
	long	*minimumAwarenessTime;	/* OPTIONAL */
	struct LanePositions	*applicableLanes;	/* OPTIONAL */
	IviType_t	 iviType;
	IviPurpose_t	*iviPurpose;	/* OPTIONAL */
	LaneStatus_t	*laneStatus;	/* OPTIONAL */
	struct VehicleCharacteristicsList	*vehicleCharacteristics;	/* OPTIONAL */
	IVI_DriverCharacteristics_t	*driverCharacteristics;	/* OPTIONAL */
	long	*layoutId;	/* OPTIONAL */
	long	*preStoredlayoutId;	/* OPTIONAL */
	RoadSignCodes_t	 roadSignCodes;
	struct ConstraintTextLines1	*extraText;	/* OPTIONAL */
	/*
	 * This type is extensible,
	 * possible extensions are below.
	 */
	
	/* Context for parsing across buffer boundaries */
	asn_struct_ctx_t _asn_ctx;
} GicPart_t;

/* Implementation */
extern asn_TYPE_descriptor_t asn_DEF_GicPart;
extern asn_SEQUENCE_specifics_t asn_SPC_GicPart_specs_1;
extern asn_TYPE_member_t asn_MBR_GicPart_1[16];

#ifdef __cplusplus
}
#endif

/* Referred external types */
#include "ZoneIds.h"
#include "VarLengthNumber.h"
#include "LanePositions.h"
#include "VehicleCharacteristicsList.h"
#include "ConstraintTextLines1.h"

#endif	/* _GicPart_H_ */
#include "asn_internal.h"
