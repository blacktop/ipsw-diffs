## CoreODI

> `/System/Library/PrivateFrameworks/CoreODI.framework/CoreODI`

```diff

-5.0.25.0.0
-  __TEXT.__text: 0x4617c
+5.1.1.0.0
+  __TEXT.__text: 0x4603c
   __TEXT.__auth_stubs: 0x16c0
   __TEXT.__objc_methlist: 0x254
   __TEXT.__const: 0x1092
   __TEXT.__gcc_except_tab: 0x50
-  __TEXT.__cstring: 0x7e8a
+  __TEXT.__cstring: 0x7faa
   __TEXT.__oslogstring: 0x471
   __TEXT.__constg_swiftt: 0x7ec
   __TEXT.__swift5_typeref: 0x70b

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: D2623489-C65C-32C1-AE33-894CD4A2C4D0
+  UUID: E1056DAC-B993-3841-A72B-59417EABCB0A
   Functions: 913
   Symbols:   693
   CStrings:  642
Functions:
~ sub_2440d2458 -> sub_245693458 : 40504 -> 40184
CStrings:
+ "[\n    {\n        \"identifier\": \"software_version\",\n        \"fieldName\": \"BuildVersion\",\n        \"source\": \"MobileGestalt\",\n        \"priority\": 2\n    },\n    {\n        \"identifier\": \"os_version_baa_cert\",\n        \"fieldName\": \"osVersion\",\n        \"source\": \"baaCertificate\",\n        \"priority\": 2,\n        \"timeoutMilli\": 1500\n    },\n    {\n        \"identifier\": \"time_zone\",\n        \"fieldName\": \"identifier\",\n        \"source\": \"TimeZone\",\n        \"priority\": 1\n    },\n    {\n        \"identifier\": \"unsigned_seid\",\n        \"fieldName\": \"seid\",\n        \"source\": \"NearField\",\n        \"priority\": 2,\n        \"privileged\": true\n    },\n    {\n        \"identifier\": \"signed_seid\",\n        \"fieldName\": \"seid\",\n        \"source\": \"baaCertificate\",\n        \"priority\": 2,\n        \"timeoutMilli\": 1500\n    },\n    {\n        \"identifier\": \"unsigned_serial_number\",\n        \"fieldName\": \"SerialNumber\",\n        \"source\": \"MobileGestalt\",\n        \"priority\": 1,\n        \"privileged\": true\n    },\n    {\n        \"identifier\": \"unsigned_udid\",\n        \"fieldName\": \"UniqueDeviceID\",\n        \"source\": \"MobileGestalt\",\n        \"priority\": 1,\n        \"privileged\": true\n    },\n    {\n        \"identifier\": \"unsigned_ecid\",\n        \"fieldName\": \"UniqueChipID\",\n        \"source\": \"MobileGestalt\",\n        \"priority\": 2,\n        \"privileged\": true\n    },\n    {\n        \"identifier\": \"ecid_baa_certified\",\n        \"fieldName\": \"ECID\",\n        \"source\": \"baaCertificate\",\n        \"priority\": 2,\n        \"timeoutMilli\": 1500\n    },\n    {\n        \"identifier\": \"phone_number_device\",\n        \"fieldName\": \"number\",\n        \"source\": \"CoreTelephony\",\n        \"priority\": 2\n    },\n    {\n        \"identifier\": \"pac_data_list\",\n        \"fieldName\": \"serverVerifiableEncoding\",\n        \"source\": \"IDS\",\n        \"priority\": 1,\n        \"privileged\": true\n    },\n    {\n        \"identifier\": \"gps_location\",\n        \"fieldName\": \"location\",\n        \"source\": \"CoreLocation\",\n        \"priority\": 2\n    },\n    {\n        \"identifier\": \"gps_location_enabled\",\n        \"fieldName\": \"locationServicesEnabled\",\n        \"source\": \"CoreLocation\",\n        \"priority\": 2\n    }\n]"
- "[\n    {\n        \"identifier\": \"software_version\",\n        \"fieldName\": \"BuildVersion\",\n        \"source\": \"MobileGestalt\",\n        \"priority\": 2\n    },\n    {\n        \"identifier\": \"os_version_baa_cert\",\n        \"fieldName\": \"osVersion\",\n        \"source\": \"baaCertificate\",\n        \"priority\": 2,\n        \"timeoutMilli\": 1500\n    },\n    {\n        \"identifier\": \"time_zone\",\n        \"fieldName\": \"identifier\",\n        \"source\": \"TimeZone\",\n        \"priority\": 1\n    },\n    {\n        \"identifier\": \"unsigned_seid\",\n        \"fieldName\": \"seid\",\n        \"source\": \"NearField\",\n        \"priority\": 2,\n        \"privileged\": true\n    },\n    {\n        \"identifier\": \"signed_seid\",\n        \"fieldName\": \"seid\",\n        \"source\": \"baaCertificate\",\n        \"priority\": 2,\n        \"timeoutMilli\": 1500\n    },\n    {\n        \"identifier\": \"unsigned_serial_number\",\n        \"fieldName\": \"SerialNumber\",\n        \"source\": \"MobileGestalt\",\n        \"priority\": 1,\n        \"privileged\": true\n    },\n    {\n        \"identifier\": \"unsigned_udid\",\n        \"fieldName\": \"UniqueDeviceID\",\n        \"source\": \"MobileGestalt\",\n        \"priority\": 1,\n        \"privileged\": true\n    },\n    {\n        \"identifier\": \"unsigned_ecid\",\n        \"fieldName\": \"UniqueChipID\",\n        \"source\": \"MobileGestalt\",\n        \"priority\": 2,\n        \"privileged\": true\n    },\n    {\n        \"identifier\": \"ecid_baa_certified\",\n        \"fieldName\": \"ECID\",\n        \"source\": \"baaCertificate\",\n        \"priority\": 2,\n        \"timeoutMilli\": 1500\n    },\n    {\n        \"identifier\": \"phone_number_device\",\n        \"fieldName\": \"number\",\n        \"source\": \"CoreTelephony\",\n        \"priority\": 2\n    },\n    {\n        \"identifier\": \"pac_data_list\",\n        \"fieldName\": \"serverVerifiableEncoding\",\n        \"source\": \"IDS\",\n        \"priority\": 1,\n        \"privileged\": true\n    }\n]"

```
