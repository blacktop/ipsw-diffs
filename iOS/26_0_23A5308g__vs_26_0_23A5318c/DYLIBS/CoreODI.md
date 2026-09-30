## CoreODI

> `/System/Library/PrivateFrameworks/CoreODI.framework/CoreODI`

```diff

-5.0.24.0.0
-  __TEXT.__text: 0x466ac
+5.0.25.0.0
+  __TEXT.__text: 0x460b8
   __TEXT.__auth_stubs: 0x16c0
   __TEXT.__objc_methlist: 0x254
   __TEXT.__const: 0x1092
   __TEXT.__gcc_except_tab: 0x50
-  __TEXT.__cstring: 0x734a
+  __TEXT.__cstring: 0x7e8a
   __TEXT.__oslogstring: 0x471
   __TEXT.__constg_swiftt: 0x7ec
   __TEXT.__swift5_typeref: 0x70b

   __TEXT.__objc_methname: 0x589
   __TEXT.__objc_methtype: 0xe0
   __TEXT.__objc_stubs: 0x240
-  __DATA_CONST.__got: 0x498
+  __DATA_CONST.__got: 0x4a0
   __DATA_CONST.__const: 0x570
   __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_protolist: 0x10

   __AUTH_CONST.__objc_const: 0xf68
   __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x14
-  __DATA.__data: 0x208
+  __DATA.__data: 0x200
   __DATA.__common: 0x28
   __DATA.__bss: 0xd80
   __DATA_DIRTY.__objc_data: 0x568
-  __DATA_DIRTY.__data: 0xd28
+  __DATA_DIRTY.__data: 0xd30
   __DATA_DIRTY.__bss: 0x3a0
   __DATA_DIRTY.__common: 0xa8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: FABF7D7F-A310-3D3D-B284-89F13BA466EF
+  UUID: F5415259-D9FC-3D94-896C-F78B6885F6A5
   Functions: 913
   Symbols:   693
-  CStrings:  639
+  CStrings:  642
 
Functions:
~ sub_24387c370 -> sub_2437d7370 : 4080 -> 4272
~ sub_24389b30c -> sub_2437f63cc : 42220 -> 40504
CStrings:
+ "[\n  {\n    \"identifier\": \"icloud_dsid\",\n    \"fieldName\": \"aa_personID\",\n    \"source\": \"Accounts\",\n    \"priority\": 1,\n    \"privileged\": true\n  },\n  {\n    \"identifier\": \"signed_seid\",\n    \"fieldName\": \"seid\",\n    \"source\": \"baaCertificate\",\n    \"priority\": 2,\n    \"timeoutMilli\": 1500\n  },\n  {\n    \"identifier\": \"unsigned_seid\",\n    \"fieldName\": \"seid\",\n    \"source\": \"NearField\",\n    \"priority\": 2,\n    \"privileged\": true\n  },\n  {\n    \"identifier\": \"ecid_baa_certified\",\n    \"fieldName\": \"ECID\",\n    \"source\": \"baaCertificate\",\n    \"priority\": 2,\n    \"timeoutMilli\": 1500\n  },\n  {\n    \"identifier\": \"unsigned_ecid\",\n    \"fieldName\": \"UniqueChipID\",\n    \"source\": \"MobileGestalt\",\n    \"priority\": 2,\n    \"privileged\": true\n  },\n  {\n    \"identifier\": \"os_version_baa_cert\",\n    \"fieldName\": \"osVersion\",\n    \"source\": \"baaCertificate\",\n    \"priority\": 2,\n    \"timeoutMilli\": 1500\n  },\n  {\n    \"identifier\": \"time_zone\",\n    \"fieldName\": \"identifier\",\n    \"source\": \"TimeZone\",\n    \"priority\": 1\n  },\n  {\n    \"identifier\": \"gps_location_enabled\",\n    \"fieldName\": \"locationServicesEnabled\",\n    \"source\": \"CoreLocation\",\n    \"priority\": 2\n  },\n  {\n    \"identifier\": \"screen_share_status\",\n    \"fieldName\": \"isSharingScreen\",\n    \"source\": \"TelephonyUtilities\",\n    \"priority\": 1,\n    \"privileged\": true\n  },\n  {\n    \"identifier\": \"pac_data_list\",\n    \"fieldName\": \"serverVerifiableEncoding\",\n    \"source\": \"IDS\",\n    \"priority\": 1,\n    \"privileged\": true\n  }\n]"
+ "[\n  {\n    \"identifier\": \"pac_data_list\",\n    \"fieldName\": \"serverVerifiableEncoding\",\n    \"source\": \"IDS\",\n    \"priority\": 1,\n    \"privileged\": true\n  },\n  {\n    \"identifier\": \"signed_seid\",\n    \"fieldName\": \"seid\",\n    \"source\": \"baaCertificate\",\n    \"priority\": 2,\n    \"timeoutMilli\": 1500\n  },\n  {\n    \"identifier\": \"phone_number_device\",\n    \"fieldName\": \"number\",\n    \"source\": \"CoreTelephony\",\n    \"priority\": 2\n  },\n  {\n    \"identifier\": \"gps_location_enabled\",\n    \"fieldName\": \"locationServicesEnabled\",\n    \"source\": \"CoreLocation\",\n    \"priority\": 2\n  },\n  {\n    \"identifier\": \"software_version\",\n    \"fieldName\": \"BuildVersion\",\n    \"source\": \"MobileGestalt\",\n    \"priority\": 3\n  },\n  {\n    \"identifier\": \"unsigned_serial_number\",\n    \"fieldName\": \"SerialNumber\",\n    \"source\": \"MobileGestalt\",\n    \"priority\": 1,\n    \"privileged\": true\n  },\n  {\n    \"identifier\": \"unsigned_ecid\",\n    \"fieldName\": \"UniqueChipID\",\n    \"source\": \"MobileGestalt\",\n    \"priority\": 2,\n    \"privileged\": true\n  },\n  {\n    \"identifier\": \"time_zone\",\n    \"fieldName\": \"identifier\",\n    \"source\": \"TimeZone\",\n    \"priority\": 2\n  }\n]"
+ "[\n  {\n    \"identifier\": \"pac_data_list\",\n    \"fieldName\": \"serverVerifiableEncoding\",\n    \"source\": \"IDS\",\n    \"priority\": 1,\n    \"privileged\": true\n  },\n  {\n    \"identifier\": \"signed_seid\",\n    \"fieldName\": \"seid\",\n    \"source\": \"baaCertificate\",\n    \"priority\": 2,\n    \"timeoutMilli\": 1500\n  },\n  {\n    \"identifier\": \"phone_number_device\",\n    \"fieldName\": \"number\",\n    \"source\": \"CoreTelephony\",\n    \"priority\": 2\n  },\n  {\n    \"identifier\": \"gps_location_enabled\",\n    \"fieldName\": \"locationServicesEnabled\",\n    \"source\": \"CoreLocation\",\n    \"priority\": 2\n  },\n  {\n    \"identifier\": \"software_version\",\n    \"fieldName\": \"BuildVersion\",\n    \"source\": \"MobileGestalt\",\n    \"priority\": 3\n  },\n  {\n    \"identifier\": \"unsigned_serial_number\",\n    \"fieldName\": \"SerialNumber\",\n    \"source\": \"MobileGestalt\",\n    \"priority\": 1,\n    \"privileged\": true\n  },\n  {\n    \"identifier\": \"unsigned_ecid\",\n    \"fieldName\": \"UniqueChipID\",\n    \"source\": \"MobileGestalt\",\n    \"priority\": 2,\n    \"privileged\": true\n  },\n  {\n    \"identifier\": \"time_zone\",\n    \"fieldName\": \"identifier\",\n    \"source\": \"TimeZone\",\n    \"priority\": 2\n  },\n  {\n    \"identifier\": \"dust_cloud_indicator\",\n    \"fieldName\": \"isPairingInitiated\",\n    \"source\": \"DeviceSettings\",\n    \"priority\": 2\n  }\n]"
+ "dust_cloud_indicator"
- "[\n  {\n    \"identifier\": \"pac_data_list\",\n    \"fieldName\": \"serverVerifiableEncoding\",\n    \"source\": \"IDS\",\n    \"priority\": 1,\n    \"privileged\": true\n  },\n  {\n    \"identifier\": \"phone_number_device\",\n    \"fieldName\": \"number\",\n    \"source\": \"CoreTelephony\",\n    \"priority\": 2\n  },\n  {\n    \"identifier\": \"gps_location_enabled\",\n    \"fieldName\": \"locationServicesEnabled\",\n    \"source\": \"CoreLocation\",\n    \"priority\": 2\n  },\n  {\n    \"identifier\": \"software_version\",\n    \"fieldName\": \"BuildVersion\",\n    \"source\": \"MobileGestalt\",\n    \"priority\": 3\n  },\n  {\n    \"identifier\": \"unsigned_serial_number\",\n    \"fieldName\": \"SerialNumber\",\n    \"source\": \"MobileGestalt\",\n    \"priority\": 1,\n    \"privileged\": true\n  },\n  {\n    \"identifier\": \"unsigned_ecid\",\n    \"fieldName\": \"UniqueChipID\",\n    \"source\": \"MobileGestalt\",\n    \"priority\": 2,\n    \"privileged\": true\n  },\n  {\n    \"identifier\": \"time_zone\",\n    \"fieldName\": \"identifier\",\n    \"source\": \"TimeZone\",\n    \"priority\": 2\n  }\n]"

```
