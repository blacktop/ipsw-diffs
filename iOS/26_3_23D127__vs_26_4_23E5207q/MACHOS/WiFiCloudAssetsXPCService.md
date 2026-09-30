## WiFiCloudAssetsXPCService

> `/System/Library/PrivateFrameworks/WiFiPolicy.framework/XPCServices/WiFiCloudAssetsXPCService.xpc/WiFiCloudAssetsXPCService`

```diff

-1035.6.0.0.0
-  __TEXT.__text: 0x7568
-  __TEXT.__auth_stubs: 0x330
-  __TEXT.__objc_stubs: 0x1280
+1041.19.2.0.0
+  __TEXT.__text: 0x76d0
+  __TEXT.__auth_stubs: 0x340
+  __TEXT.__objc_stubs: 0x10a0
   __TEXT.__objc_methlist: 0x520
-  __TEXT.__cstring: 0x140a
-  __TEXT.__objc_classname: 0xac
-  __TEXT.__objc_methname: 0x1335
-  __TEXT.__objc_methtype: 0x22c
+  __TEXT.__objc_methname: 0xfe7
+  __TEXT.__cstring: 0x152a
+  __TEXT.__objc_classname: 0xd9
+  __TEXT.__objc_methtype: 0x20c
   __TEXT.__const: 0x20
-  __TEXT.__unwind_info: 0x178
-  __DATA_CONST.__auth_got: 0x1a0
-  __DATA_CONST.__got: 0x108
-  __DATA_CONST.__const: 0x1108
-  __DATA_CONST.__cfstring: 0x16e0
-  __DATA_CONST.__objc_classlist: 0x28
+  __TEXT.__unwind_info: 0x138
+  __DATA_CONST.__auth_got: 0x1a8
+  __DATA_CONST.__got: 0xf8
+  __DATA_CONST.__const: 0x11c8
+  __DATA_CONST.__cfstring: 0x1800
+  __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x8
-  __DATA_CONST.__objc_arraydata: 0x8
-  __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_const: 0xa78
-  __DATA.__objc_selrefs: 0x648
-  __DATA.__objc_ivar: 0x80
-  __DATA.__objc_data: 0x190
+  __DATA_CONST.__objc_superrefs: 0x20
+  __DATA.__objc_const: 0x9d8
+  __DATA.__objc_selrefs: 0x588
+  __DATA.__objc_ivar: 0x58
+  __DATA.__objc_data: 0x230
   __DATA.__data: 0x130
   __DATA.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 575168BE-99B8-3C6D-AC6F-0E51427342F3
-  Functions: 104
-  Symbols:   127
-  CStrings:  698
+  UUID: BDBC95B7-A41A-37D4-A033-D94F84F1D9BA
+  Functions: 98
+  Symbols:   133
+  CStrings:  671
 
Symbols:
+ _OBJC_CLASS_$_NSSet
+ _OBJC_CLASS_$_WCAFetchRequest
+ _OBJC_CLASS_$_WCAFetchResponse
+ _OBJC_METACLASS_$_WCAFetchKeyValuesResponse
+ _OBJC_METACLASS_$_WCAFetchRequest
+ _OBJC_METACLASS_$_WCAFetchResponse
+ _OBJC_METACLASS_$_WCAFetchSQLiteRequest
+ _OBJC_METACLASS_$_WCAFetchSQLiteResponse
+ _objc_setProperty_nonatomic_copy
- _OBJC_CLASS_$_NSConstantArray
- _OBJC_CLASS_$_WCAFetchBeaconDBParameters
- _OBJC_METACLASS_$_WCAFetchBeaconDBParameters
CStrings:
+ "%s Error: Response is not of type WCAFetchKeyValuesResponse, instead its %@"
+ "+[WCAFetchWiFiBehaviorParameters fetchWiFiBehaviorWithCompletion:]_block_invoke"
+ "245326d2-3ddb-4c46-a08e-aab8b6060a1b"
+ "85ff7a90-361b-42d1-a420-97dee860f018"
+ "97d68e5c-95bb-4136-9aa0-f08964fcc0e1"
+ "<%@ : %p "
+ ">"
+ "ForceMABrainUpdate"
+ "MABrainLoadError"
+ "T@\"NSArray\",C,N,V_columnNames"
+ "T@\"NSArray\",C,N,V_records"
+ "T@\"NSDictionary\",C,N,V_keyValues"
+ "T@\"NSDictionary\",C,N,V_parameters"
+ "T@\"NSString\",C,N,V_tableName"
+ "Tq,N,V_limit"
+ "WCAFetchKeyValuesResponse"
+ "WCAFetchSQLiteRequest"
+ "WCAFetchSQLiteResponse"
+ "_columnNames"
+ "_keyValues"
+ "_limit"
+ "_parameters"
+ "_records"
+ "_tableName"
+ "allValues"
+ "appendString:"
+ "b1f792b1-0797-48f1-8603-107cefcf1d45"
+ "columnNames: %@"
+ "copy"
+ "customer"
+ "decodeIntegerForKey:"
+ "decodeObjectOfClass:forKey:"
+ "decodeObjectOfClasses:forKey:"
+ "ed5a1c1d-2a39-4993-8bcc-f260c4b42868"
+ "encodeInteger:forKey:"
+ "encodeObject:forKey:"
+ "encodeWithCoder:"
+ "external-pre-release"
+ "fb333b76-b463-401f-8899-96d82fc4c598"
+ "initWithCoder:"
+ "key/values: %@"
+ "limit: %ld"
+ "livable"
+ "parameters: %@"
+ "records: %@"
+ "seed-staging"
+ "setKeyValues:"
+ "setRecords:"
+ "setWithObjects:"
+ "supportsSecureCoding"
+ "tableName: %@"
+ "untested"
- "11c_antennas"
- "11n_antennas"
- "Error: Response is not of type WCAFetchKeyValuesResponse, instead its %@"
- "QBSS_Load"
- "T@\"NSString\",&,N,V_antennas11n"
- "T@\"NSString\",&,N,V_wlanAsel"
- "T@\"NSString\",&,N,V_wlanFixedCapabilities"
- "T@\"NSString\",&,N,V_wlanHTAmpduparam"
- "T@\"NSString\",&,N,V_wlanHTCapabilities"
- "T@\"NSString\",&,N,V_wlanHtexCapabilities"
- "T@\"NSString\",&,N,V_wlanTxbf"
- "T@\"NSString\",&,N,V_wlanVhtCapabilities"
- "T@\"NSString\",&,N,V_wlanWfaIeWmeQosInfo"
- "TB,N,V_QBSS_Load"
- "TB,N,V_UAPSD"
- "TB,N,V_has_11krm"
- "Tf,N,V_antennas11c"
- "Tf,N,V_max_rates"
- "Tf,N,V_wlanTimDtimPeriod"
- "Tq,N,V_beaconInterval"
- "U-APSD"
- "UAPSD"
- "WCAFetchBeaconDBParameters"
- "_QBSS_Load"
- "_UAPSD"
- "_antennas11c"
- "_antennas11n"
- "_beaconInterval"
- "_has_11krm"
- "_max_rates"
- "_wlanAsel"
- "_wlanFixedCapabilities"
- "_wlanHTAmpduparam"
- "_wlanHTCapabilities"
- "_wlanHtexCapabilities"
- "_wlanTimDtimPeriod"
- "_wlanTxbf"
- "_wlanVhtCapabilities"
- "_wlanWfaIeWmeQosInfo"
- "antennas11c"
- "antennas11n"
- "beaconInterval"
- "beacon_interval"
- "f16@0:8"
- "fetchWithCompletion:"
- "has_11krm"
- "index"
- "max_rates"
- "numberWithBool:"
- "numberWithFloat:"
- "numberWithLong:"
- "prof_clean"
- "setAntennas11c:"
- "setAntennas11n:"
- "setBeaconInterval:"
- "setHas_11krm:"
- "setMax_rates:"
- "setQBSS_Load:"
- "setUAPSD:"
- "setValue:forKey:"
- "setWlanAsel:"
- "setWlanFixedCapabilities:"
- "setWlanHTAmpduparam:"
- "setWlanHTCapabilities:"
- "setWlanHtexCapabilities:"
- "setWlanTimDtimPeriod:"
- "setWlanTxbf:"
- "setWlanVhtCapabilities:"
- "setWlanWfaIeWmeQosInfo:"
- "v20@0:8B16"
- "v20@0:8f16"
- "valueForKey:"
- "wlan-asel"
- "wlan-fixed-capabilities"
- "wlan-ht-ampduparam"
- "wlan-ht-capabilities"
- "wlan-htex-capabilities"
- "wlan-tim-dtim_period"
- "wlan-txbf"
- "wlan-vht-capabilities"
- "wlan-wfa-ie-wme-qos_info"
- "wlanAsel"
- "wlanFixedCapabilities"
- "wlanHTAmpduparam"
- "wlanHTCapabilities"
- "wlanHtexCapabilities"
- "wlanTimDtimPeriod"
- "wlanTxbf"
- "wlanVhtCapabilities"
- "wlanWfaIeWmeQosInfo"

```
