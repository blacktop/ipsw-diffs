## HealthKit

> `/System/Library/Frameworks/HealthKit.framework/HealthKit`

```diff

-5200.2.4.1.5
-  __TEXT.__text: 0x2b2f4c
+5200.2.7.1.3
+  __TEXT.__text: 0x2b32f8
   __TEXT.__auth_stubs: 0x3150
-  __TEXT.__objc_methlist: 0x2a648
-  __TEXT.__cstring: 0x2f319
-  __TEXT.__const: 0xa3e90
-  __TEXT.__oslogstring: 0xbc14
-  __TEXT.__gcc_except_tab: 0x3e94
+  __TEXT.__objc_methlist: 0x2a6e8
+  __TEXT.__cstring: 0x2f309
+  __TEXT.__const: 0xa3ef0
+  __TEXT.__oslogstring: 0xbc84
+  __TEXT.__gcc_except_tab: 0x3e9c
   __TEXT.__ustring: 0x7e
   __TEXT.__dlopen_cstrs: 0x638
   __TEXT.__swift5_typeref: 0x14db

   __TEXT.__swift5_types: 0x1e4
   __TEXT.__swift5_protos: 0x10
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0xd7d8
+  __TEXT.__unwind_info: 0xd7e8
   __TEXT.__eh_frame: 0x1f78
-  __TEXT.__objc_classname: 0x867b
-  __TEXT.__objc_methname: 0x59a29
-  __TEXT.__objc_methtype: 0xbc09
-  __TEXT.__objc_stubs: 0x28dc0
-  __DATA_CONST.__got: 0x19a0
-  __DATA_CONST.__const: 0xe648
-  __DATA_CONST.__objc_classlist: 0x19d0
+  __TEXT.__objc_classname: 0x868d
+  __TEXT.__objc_methname: 0x59ba5
+  __TEXT.__objc_methtype: 0xbbf0
+  __TEXT.__objc_stubs: 0x28e20
+  __DATA_CONST.__got: 0x19a8
+  __DATA_CONST.__const: 0xe600
+  __DATA_CONST.__objc_classlist: 0x19d8
   __DATA_CONST.__objc_catlist: 0x1c8
   __DATA_CONST.__objc_protolist: 0x7d0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x10618
+  __DATA_CONST.__objc_selrefs: 0x10678
   __DATA_CONST.__objc_protorefs: 0x5f0
-  __DATA_CONST.__objc_superrefs: 0x16b0
+  __DATA_CONST.__objc_superrefs: 0x16b8
   __DATA_CONST.__objc_arraydata: 0x68a8
   __AUTH_CONST.__auth_got: 0x18c0
   __AUTH_CONST.__auth_ptr: 0x838
-  __AUTH_CONST.__const: 0x6e50
-  __AUTH_CONST.__cfstring: 0x2fc40
-  __AUTH_CONST.__objc_const: 0x52a28
+  __AUTH_CONST.__const: 0x6e10
+  __AUTH_CONST.__cfstring: 0x2fc80
+  __AUTH_CONST.__objc_const: 0x52b48
   __AUTH_CONST.__objc_intobj: 0x44e8
   __AUTH_CONST.__objc_dictobj: 0x488
   __AUTH_CONST.__objc_doubleobj: 0x140
   __AUTH_CONST.__objc_arrayobj: 0x6a8
-  __AUTH.__objc_data: 0xe038
-  __AUTH.__data: 0x1040
-  __DATA.__objc_ivar: 0x2c28
+  __AUTH.__objc_data: 0xe0d8
+  __AUTH.__data: 0x10c8
+  __DATA.__objc_ivar: 0x2c38
   __DATA.__data: 0xaee8
   __DATA.__bss: 0x9020
   __DATA.__common: 0x988
-  __DATA_DIRTY.__objc_data: 0x24a0
-  __DATA_DIRTY.__data: 0xe8
+  __DATA_DIRTY.__objc_data: 0x2450
+  __DATA_DIRTY.__data: 0x78
   __DATA_DIRTY.__bss: 0xba0
   __DATA_DIRTY.__common: 0xf0
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 20078
-  Symbols:   21458
-  CStrings:  22353
+  Functions: 20092
+  Symbols:   21476
+  CStrings:  22365
 
Symbols:
+ _HKMetadataKeyAppleFitnessPlusCatalogIdentifier
+ _OBJC_CLASS_$_CTStewieStateMonitor
+ _OBJC_CLASS_$_HKCoreTelephonySatelliteClient
+ _OBJC_METACLASS_$_HKCoreTelephonySatelliteClient
CStrings:
+ "@\"<HKCoreTelephonySatelliteClientDelegate>\""
+ "@\"CTStewieState\""
+ "@\"CTStewieStateMonitor\""
+ "CTStewieStateMonitorDelegate"
+ "HKCoreTelephonySatelliteClient"
+ "HKMetadataKeyAppleFitnessPlusCatalogIdentifier"
+ "T@\"<HKCoreTelephonySatelliteClientDelegate>\",W,N,V_delegate"
+ "T@\"CTStewieState\",&,N,V_cachedStewieState"
+ "T@\"CTStewieStateMonitor\",&,N,V_stewieStateMonitor"
+ "TB,N,V_isRealityDevice"
+ "[%!@(MISSING)][Satellite Support] Fetched satellite support as: %!d(MISSING)"
+ "[%!@(MISSING)][Satellite Support] Satellite support changed"
+ "_cachedStewieState"
+ "_stewieStateMonitor"
+ "_supportsMedicalIDSync"
+ "cachedStewieState"
+ "fetchAllSourcesContainingDataWithCompletion:"
+ "fetchUserHasAgreedToHealthRecordsDataSubmissionWithCompletion:"
+ "getState"
+ "isDemoAllowedForService:"
+ "isSatelliteSupportedForEmergencyDemo"
+ "remote_fetchAllSourcesContainingDataWithCompletion:"
+ "remote_fetchUserHasAgreedToHealthRecordsDataSubmissionWithCompletion:"
+ "satelliteSupportChanged:"
+ "setCachedStewieState:"
+ "setIsIOSDevice:"
+ "setStewieStateMonitor:"
+ "setSupportsMedicalIDSync:"
+ "stateChanged:"
+ "stewieStateMonitor"
+ "supportsMedicalIDSync"
+ "v24@0:8@\"CTStewieState\"16"
- "-[HKCoreTelephonyClient stewieSupportChanged]"
- "@\"<HKCoreTelephonyClientDelegate>\""
- "@\"CTStewieSupport\""
- "CoreTelephonyClientProvisioningDelegate"
- "T@\"<HKCoreTelephonyClientDelegate>\",W,N,V_delegate"
- "_cachedStewieSupport"
- "dedicatedBearedRemoved:"
- "dedicatedBearerAdded:success:"
- "dedicatedBearerSupportChanged:"
- "fetchStewieSupportedWithCompletion:"
- "getStewieSupportWithCompletion:"
- "qoSLinkCharacteristicsChanged:"
- "satelliteMsgCfgChanged"
- "stewieSupportChanged"
- "stewieSupportChanged:"
- "transportKeysChanged"
- "v24@0:8@\"CTQoSLinkCharacteristics\"16"
- "v24@0:8@\"NSString\"16"
- "v24@?0@\"CTStewieSupport\"8@\"NSError\"16"
- "v28@0:8@\"NSString\"16B24"

```
