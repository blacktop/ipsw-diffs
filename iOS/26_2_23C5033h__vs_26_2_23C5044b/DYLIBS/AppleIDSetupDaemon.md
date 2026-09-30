## AppleIDSetupDaemon

> `/System/Library/PrivateFrameworks/AppleIDSetupDaemon.framework/AppleIDSetupDaemon`

```diff

-82.250.6.0.0
-  __TEXT.__text: 0x1057f8
-  __TEXT.__auth_stubs: 0x2920
+82.250.11.0.0
+  __TEXT.__text: 0x109aa0
+  __TEXT.__auth_stubs: 0x2980
   __TEXT.__objc_methlist: 0x6fc
-  __TEXT.__const: 0x3e24
+  __TEXT.__const: 0x3e54
   __TEXT.__cstring: 0x1872
-  __TEXT.__oslogstring: 0x7a0f
-  __TEXT.__constg_swiftt: 0x1c10
-  __TEXT.__swift5_typeref: 0x1be0
+  __TEXT.__oslogstring: 0x7c8f
+  __TEXT.__constg_swiftt: 0x1c28
+  __TEXT.__swift5_typeref: 0x1c8e
   __TEXT.__swift5_reflstr: 0xe9e
   __TEXT.__swift5_fieldmd: 0xe30
   __TEXT.__swift5_builtin: 0xa0
   __TEXT.__swift5_assocty: 0x2a0
   __TEXT.__swift5_proto: 0x194
   __TEXT.__swift5_types: 0x100
-  __TEXT.__swift_as_entry: 0x380
-  __TEXT.__swift_as_ret: 0x6b4
-  __TEXT.__swift5_capture: 0x898
+  __TEXT.__swift_as_entry: 0x390
+  __TEXT.__swift_as_ret: 0x6d4
+  __TEXT.__swift5_capture: 0x8c8
   __TEXT.__swift5_protos: 0x40
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x40a8
-  __TEXT.__eh_frame: 0xef38
+  __TEXT.__unwind_info: 0x4140
+  __TEXT.__eh_frame: 0xf380
   __TEXT.__objc_classname: 0xe6
-  __TEXT.__objc_methname: 0x14d3
+  __TEXT.__objc_methname: 0x1516
   __TEXT.__objc_methtype: 0x75a
   __TEXT.__objc_stubs: 0xc0
-  __DATA_CONST.__got: 0xbe8
+  __DATA_CONST.__got: 0xc20
   __DATA_CONST.__const: 0x120
   __DATA_CONST.__objc_classlist: 0xa8
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5f8
+  __DATA_CONST.__objc_selrefs: 0x608
   __DATA_CONST.__objc_protorefs: 0x48
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x1498
-  __AUTH_CONST.__const: 0x27a8
+  __AUTH_CONST.__auth_got: 0x14c8
+  __AUTH_CONST.__const: 0x27d0
   __AUTH_CONST.__cfstring: 0x20
   __AUTH_CONST.__objc_const: 0x3378
   __AUTH.__objc_data: 0x5c8
-  __AUTH.__data: 0xed8
+  __AUTH.__data: 0xee8
   __DATA.__objc_ivar: 0xc
-  __DATA.__data: 0x17b8
+  __DATA.__data: 0x17d8
   __DATA.__bss: 0x2d90
   __DATA.__common: 0x28
   __DATA_DIRTY.__objc_data: 0x158

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 7EC464E8-C3C9-350D-B6D9-3044123A9E27
-  Functions: 2828
-  Symbols:   1225
-  CStrings:  1020
+  UUID: D4AE5324-86D0-3A0C-BA0F-4F5FEC26BDB1
+  Functions: 2861
+  Symbols:   1232
+  CStrings:  1032
 
Symbols:
+ _AKAppleIDAuthenticationAppProvidedContextConnectDependent
+ _objectdestroy.128Tm
+ _objectdestroy.130Tm
+ _objectdestroy.133Tm
+ _symbolic SSSg
+ _symbolic Say_____G 12AppleIDSetup21BleAdvertisementFlagsV
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 12AppleIDSetup21BleAdvertisementFlagsV
+ _symbolic _____yxq_GSgXwz_________________y_____y_____GG_____Rz_____R______Rd__AI6Output______11MessageType_____RTd__AI09TransportC0______AnopQRT_r0__lXX 18AppleIDSetupDaemon18RemoteSetupServiceC AA05LocaleF0C AA27ProximityTransportConnectorC 0aB003AnyI7BuilderV AH7MessageV AH9V1CommandO AA0eF0P AA0iJ0P AH0I8BuildingP AH0P0P AH0I0P AR
- _objectdestroy.127Tm
- _objectdestroy.132Tm
CStrings:
+ "Account is signed in with valid AuthKit and iCloud accounts"
+ "Checking if teen account is already signed in on this device"
+ "Fetching family circle for existing teen account"
+ "No signed-in account found (missing primary AuthKit or iCloud service account)"
+ "Pre-populating auth context with username, making non-editable"
+ "Retrieved signed-in username from handshake: %s"
+ "Teen account already signed in on peer device, skipping family member selection"
+ "Teen signed in with username: %s"
+ "Teen without family flow detected, adding parent context"
+ "Using existing signed-in teen account with family flow"
+ "com.apple.os-eligibility-domain.change.child-and-teen-restriction-required"
+ "com.apple.os-eligibility-domain.change.unverified-adult-restriction-required"
+ "matchingServiceAccountForAuthKitAccount:service:"
+ "setSourceAltDSID:"
- "com.apple.os-eligibility-domain.change.adult-age-verification-required"
- "com.apple.os-eligibility-domain.change.teen-attached-to-family-required"

```
