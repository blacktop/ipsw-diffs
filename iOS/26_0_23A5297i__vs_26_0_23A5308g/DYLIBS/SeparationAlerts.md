## SeparationAlerts

> `/System/Library/PrivateFrameworks/SeparationAlerts.framework/SeparationAlerts`

```diff

-107.0.11.0.0
-  __TEXT.__text: 0x2e818
+107.0.12.0.0
+  __TEXT.__text: 0x2f430
   __TEXT.__auth_stubs: 0x630
-  __TEXT.__objc_methlist: 0x371c
+  __TEXT.__objc_methlist: 0x37cc
   __TEXT.__const: 0xf8
-  __TEXT.__cstring: 0x152e
-  __TEXT.__oslogstring: 0x6a0c
+  __TEXT.__cstring: 0x154a
+  __TEXT.__oslogstring: 0x6d76
   __TEXT.__gcc_except_tab: 0x24c
-  __TEXT.__unwind_info: 0x7d8
+  __TEXT.__unwind_info: 0x7f0
   __TEXT.__objc_classname: 0x5c5
-  __TEXT.__objc_methname: 0x8d48
-  __TEXT.__objc_methtype: 0x112a
-  __TEXT.__objc_stubs: 0x65e0
-  __DATA_CONST.__got: 0x2f8
+  __TEXT.__objc_methname: 0x8f28
+  __TEXT.__objc_methtype: 0x1154
+  __TEXT.__objc_stubs: 0x6760
+  __DATA_CONST.__got: 0x300
   __DATA_CONST.__const: 0x260
   __DATA_CONST.__objc_classlist: 0x100
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xf8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1d80
+  __DATA_CONST.__objc_selrefs: 0x1df8
   __DATA_CONST.__objc_superrefs: 0xe8
   __AUTH_CONST.__auth_got: 0x330
   __AUTH_CONST.__const: 0x40
-  __AUTH_CONST.__cfstring: 0x20e0
-  __AUTH_CONST.__objc_const: 0x52d8
+  __AUTH_CONST.__cfstring: 0x2100
+  __AUTH_CONST.__objc_const: 0x5338
   __AUTH_CONST.__objc_intobj: 0x1c8
   __AUTH.__objc_data: 0x140
   __AUTH.__data: 0x8
-  __DATA.__objc_ivar: 0x41c
+  __DATA.__objc_ivar: 0x424
   __DATA.__data: 0xba0
   __DATA_DIRTY.__objc_data: 0x8c0
   __DATA_DIRTY.__bss: 0x18

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A854BC3F-F70D-3F37-B067-4891A29F8925
-  Functions: 1000
-  Symbols:   3717
-  CStrings:  2452
+  UUID: 0346D606-2E0A-348F-A985-88B5CE0CB2B7
+  Functions: 1015
+  Symbols:   3762
+  CStrings:  2483
 
Symbols:
+ -[SADevice isBudForAirPodsBLECase]
+ -[SADevice isValidPartID]
+ -[SADeviceRecord getMaintenanceStatus:]
+ -[SADeviceRecord getRelationStatus:]
+ -[SADeviceRecord updateMaintenanceStatus:forDeviceWithUUID:]
+ -[SADeviceRecord updateRelationStatus:forDeviceWithUUID:]
+ -[SAMonitoringSessionManager handleMultiPartStatusEvent:]
+ -[SAMonitoringSessionManager isBudPartID:inCasePartID:relationStatus:]
+ -[SAMonitoringSessionManager shouldSuppressBudsAlertDueToCaseLeashedNotAdv:]
+ -[SASingleDeviceRecord maintenanceStatus]
+ -[SASingleDeviceRecord relationStatus]
+ -[SASingleDeviceRecord setMaintenanceStatus:]
+ -[SASingleDeviceRecord setRelationStatus:]
+ -[SASingleDeviceRecord updateMaintenanceStatus:]
+ -[SASingleDeviceRecord updateRelationStatus:]
+ _OBJC_CLASS_$_TAMultiPartStatus
+ _OBJC_IVAR_$_SASingleDeviceRecord._maintenanceStatus
+ _OBJC_IVAR_$_SASingleDeviceRecord._relationStatus
+ _objc_msgSend$getRelationStatus:
+ _objc_msgSend$handleMultiPartStatusEvent:
+ _objc_msgSend$isBudForAirPodsBLECase
+ _objc_msgSend$isBudPartID:inCasePartID:relationStatus:
+ _objc_msgSend$isValidPartID
+ _objc_msgSend$maintenanceStatus
+ _objc_msgSend$relationStatus
+ _objc_msgSend$shouldSuppressBudsAlertDueToCaseLeashedNotAdv:
+ _objc_msgSend$updateMaintenanceStatus:
+ _objc_msgSend$updateMaintenanceStatus:forDeviceWithUUID:
+ _objc_msgSend$updateRelationStatus:
+ _objc_msgSend$updateRelationStatus:forDeviceWithUUID:
CStrings:
+ "Tq,N,V_maintenanceStatus"
+ "Tq,N,V_relationStatus"
+ "_maintenanceStatus"
+ "_relationStatus"
+ "caseLeashedNotAdvSuppressed"
+ "getMaintenanceStatus:"
+ "getRelationStatus:"
+ "handleMultiPartStatusEvent:"
+ "isBudForAirPodsBLECase"
+ "isBudPartID:inCasePartID:relationStatus:"
+ "isValidPartID"
+ "maintenanceStatus"
+ "q40@0:8q16q24q32"
+ "relationStatus"
+ "setMaintenanceStatus:"
+ "setRelationStatus:"
+ "shouldSuppressBudsAlertDueToCaseLeashedNotAdv:"
+ "updateMaintenanceStatus:"
+ "updateMaintenanceStatus:forDeviceWithUUID:"
+ "updateRelationStatus:"
+ "updateRelationStatus:forDeviceWithUUID:"
+ "v20@0:8C16"
+ "v28@0:8C16@20"
+ "{\"msg%{public}.0s\":\"#sa #handleMultiPartStatusEvent event uuid nil\", \"uuid\":\"%{private}@\"}"
+ "{\"msg%{public}.0s\":\"#sa #handleMultiPartStatusEvent multi-part status\", \"uuid\":\"%{private}@\", \"name\":\"%{private}@\", \"isAirPodsCase\":\"%{private}s\", \"relation\":%{private}ld, \"maintenance\":%{private}ld}"
+ "{\"msg%{public}.0s\":\"#sa #suppress case not leashed\", \"bud\":\"%{private}@\", \"case\":\"%{private}@\"}"
+ "{\"msg%{public}.0s\":\"#sa #suppress invalid case, partID or relationStatus partID\", \"uuid\":\"%{private}@\", \"relatedCaseUUID\":\"%{private}@\"}"
+ "{\"msg%{public}.0s\":\"#sa #suppress no case found for buds\", \"uuid\":\"%{private}@\"}"
+ "{\"msg%{public}.0s\":\"#sa #suppress no related devices for buds\", \"uuid\":\"%{private}@\"}"
+ "{\"msg%{public}.0s\":\"#sa #suppress\", \"bud\":\"%{private}@\", \"budPartID\":%{private}ld, \"case\":\"%{private}@\", \"casePartID\":%{private}ld, \"relation\":%{private}ld, \"budInCase\":%{private}ld}"

```
