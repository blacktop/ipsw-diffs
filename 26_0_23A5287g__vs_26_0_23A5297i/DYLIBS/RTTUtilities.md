## RTTUtilities

> `/System/Library/PrivateFrameworks/RTTUtilities.framework/RTTUtilities`

```diff

-490.2.0.0.0
-  __TEXT.__text: 0x26cf8
-  __TEXT.__auth_stubs: 0x9c0
-  __TEXT.__objc_methlist: 0x1d00
+492.1.0.0.0
+  __TEXT.__text: 0x273f0
+  __TEXT.__auth_stubs: 0x9d0
+  __TEXT.__objc_methlist: 0x1d30
   __TEXT.__const: 0x16a
-  __TEXT.__gcc_except_tab: 0xcf8
-  __TEXT.__cstring: 0x196b
-  __TEXT.__oslogstring: 0x2f2e
+  __TEXT.__gcc_except_tab: 0xcfc
+  __TEXT.__cstring: 0x199b
+  __TEXT.__oslogstring: 0x2f8e
   __TEXT.__dlopen_cstrs: 0x279
   __TEXT.__ustring: 0x4
   __TEXT.__swift5_typeref: 0x46

   __TEXT.__swift5_reflstr: 0xb
   __TEXT.__swift5_fieldmd: 0x38
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0xa38
+  __TEXT.__unwind_info: 0xa50
   __TEXT.__eh_frame: 0x48
   __TEXT.__objc_classname: 0x247
-  __TEXT.__objc_methname: 0x5b0b
-  __TEXT.__objc_methtype: 0x898
-  __TEXT.__objc_stubs: 0x5240
+  __TEXT.__objc_methname: 0x5b5a
+  __TEXT.__objc_methtype: 0x8ee
+  __TEXT.__objc_stubs: 0x52a0
   __DATA_CONST.__got: 0x3a8
-  __DATA_CONST.__const: 0xf78
+  __DATA_CONST.__const: 0xf98
   __DATA_CONST.__objc_classlist: 0x98
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1948
+  __DATA_CONST.__objc_selrefs: 0x1960
   __DATA_CONST.__objc_superrefs: 0x78
   __DATA_CONST.__objc_arraydata: 0x190
-  __AUTH_CONST.__auth_got: 0x4f0
-  __AUTH_CONST.__const: 0x518
+  __AUTH_CONST.__auth_got: 0x4f8
+  __AUTH_CONST.__const: 0x538
   __AUTH_CONST.__cfstring: 0x18e0
-  __AUTH_CONST.__objc_const: 0x2000
+  __AUTH_CONST.__objc_const: 0x2008
   __AUTH_CONST.__objc_dictobj: 0x118
   __AUTH_CONST.__objc_intobj: 0x108
   __AUTH_CONST.__objc_arrayobj: 0xc0

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 512B5DFF-0C6E-3CEF-BF39-717E5D2E70D3
-  Functions: 836
-  Symbols:   3104
-  CStrings:  1896
+  UUID: 88129430-BE10-36EB-8507-A0036C77C0B7
+  Functions: 843
+  Symbols:   3124
+  CStrings:  1903
 
Symbols:
+ -[RTTController responseFromCallWithID:forRequest:options:]
+ -[RTTRemoteCall responseForRequest:options:].cold.1
+ -[RTTTelephonyUtilities _contactIsEmergencyServices:]
+ GCC_except_table69
+ GCC_except_table76
+ GCC_except_table90
+ GCC_except_table92
+ ___28-[RTTRemoteCall sendString:]_block_invoke.592
+ ___33-[RTTCall device:didReceiveText:]_block_invoke.416
+ ___38-[RTTDictionaryManager deleteIfNeeded]_block_invoke.279
+ ___44-[RTTRemoteCall responseForRequest:options:]_block_invoke.633
+ ___44-[RTTRemoteCall responseForRequest:options:]_block_invoke.635
+ ___44-[RTTRemoteCall responseForRequest:options:]_block_invoke.635.cold.1
+ ___48-[RTTTelephonyUtilities iCloudAccountDidChange:]_block_invoke.156
+ ___49-[RTTRemoteCall callDidReceiveText:forUtterance:]_block_invoke.609
+ ___49-[RTTRemoteCall callDidReceiveText:forUtterance:]_block_invoke.613
+ ___50-[RTTTelephonyUtilities reloadDefaultVoiceContext]_block_invoke.100
+ ___51-[RTTTelephonyUtilities listenForCloudRelayChanges]_block_invoke.151
+ ___51-[RTTTelephonyUtilities listenForCloudRelayChanges]_block_invoke.153
+ ___53-[RTTTelephonyUtilities _contactIsEmergencyServices:]_block_invoke
+ ___53-[RTTTelephonyUtilities _contactIsEmergencyServices:]_block_invoke_2
+ ___53-[RTTTelephonyUtilities _contactIsEmergencyServices:]_block_invoke_3
+ ___55-[RTTRemoteCall newRapportClientWithDestinationDevice:]_block_invoke.622
+ ___55-[RTTRemoteCall newRapportClientWithDestinationDevice:]_block_invoke.626
+ ___61-[RTTRemoteCall sendCallIDChallengeToDeviceId:orAlternateId:]_block_invoke.629
+ ___block_descriptor_32_e33_B32?0"CTXPCContextInfo"8Q16^B24l
+ ___block_literal_global.103
+ ___block_literal_global.284
+ ___block_literal_global.286
+ ___block_literal_global.577
+ ___block_literal_global.88
+ _objc_msgSend$_contactIsEmergencyServices:
+ _objc_msgSend$responseFromCallWithID:forRequest:options:
+ _objc_msgSend$slotID
+ _objc_retain_x25
- GCC_except_table65
- GCC_except_table86
- GCC_except_table88
- ___28-[RTTRemoteCall sendString:]_block_invoke.595
- ___33-[RTTCall device:didReceiveText:]_block_invoke.419
- ___38-[RTTDictionaryManager deleteIfNeeded]_block_invoke.285
- ___44-[RTTRemoteCall responseForRequest:options:]_block_invoke.636
- ___44-[RTTRemoteCall responseForRequest:options:]_block_invoke.638
- ___44-[RTTRemoteCall responseForRequest:options:]_block_invoke.638.cold.1
- ___48-[RTTTelephonyUtilities iCloudAccountDidChange:]_block_invoke.149
- ___49-[RTTRemoteCall callDidReceiveText:forUtterance:]_block_invoke.612
- ___49-[RTTRemoteCall callDidReceiveText:forUtterance:]_block_invoke.616
- ___51-[RTTTelephonyUtilities listenForCloudRelayChanges]_block_invoke.144
- ___51-[RTTTelephonyUtilities listenForCloudRelayChanges]_block_invoke.146
- ___55-[RTTRemoteCall newRapportClientWithDestinationDevice:]_block_invoke.628
- ___55-[RTTRemoteCall newRapportClientWithDestinationDevice:]_block_invoke.629
- ___61-[RTTRemoteCall sendCallIDChallengeToDeviceId:orAlternateId:]_block_invoke.632
- ___block_literal_global.287
- ___block_literal_global.289
- ___block_literal_global.580
- ___block_literal_global.84
CStrings:
+ "@\"NSDictionary\"40@0:8@\"NSString\"16@\"NSDictionary\"24@\"NSDictionary\"32"
+ "@40@0:8@16@24@32"
+ "B32@?0@\"CTXPCContextInfo\"8Q16^B24"
+ "RTTCall for %@ got request for %@. Asking delegate to help get this request to the right place."
+ "_contactIsEmergencyServices:"
+ "responseFromCallWithID:forRequest:options:"
+ "slotID"

```
