## storekitd

> `/System/Library/Frameworks/StoreKit.framework/Support/storekitd`

```diff

-814.1.5.0.0
-  __TEXT.__text: 0x2b35f0
-  __TEXT.__auth_stubs: 0x36b0
+814.1.8.0.0
+  __TEXT.__text: 0x2b4524
+  __TEXT.__auth_stubs: 0x35b0
   __TEXT.__objc_stubs: 0xcce0
-  __TEXT.__objc_methlist: 0x6d0c
-  __TEXT.__const: 0x1d270
-  __TEXT.__cstring: 0xf20a
+  __TEXT.__objc_methlist: 0x6d14
+  __TEXT.__const: 0x1da90
+  __TEXT.__cstring: 0xf485
   __TEXT.__oslogstring: 0xcb6a
   __TEXT.__objc_classname: 0x10b0
-  __TEXT.__objc_methname: 0x122c3
+  __TEXT.__objc_methname: 0x122e2
   __TEXT.__objc_methtype: 0x342a
   __TEXT.__gcc_except_tab: 0x2440
   __TEXT.__dlopen_cstrs: 0x68
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0x23ec
-  __TEXT.__swift5_typeref: 0x26b3
-  __TEXT.__swift5_reflstr: 0x16a1
-  __TEXT.__swift5_fieldmd: 0x23f0
+  __TEXT.__constg_swiftt: 0x2518
+  __TEXT.__swift5_typeref: 0x27d3
+  __TEXT.__swift5_reflstr: 0x16e1
+  __TEXT.__swift5_fieldmd: 0x2550
   __TEXT.__swift5_builtin: 0x1a4
-  __TEXT.__swift5_assocty: 0x450
-  __TEXT.__swift5_proto: 0x718
-  __TEXT.__swift5_types: 0x2e8
-  __TEXT.__swift5_capture: 0xeec
+  __TEXT.__swift5_assocty: 0x498
+  __TEXT.__swift5_proto: 0x7a8
+  __TEXT.__swift5_types: 0x314
+  __TEXT.__swift5_capture: 0xedc
   __TEXT.__swift5_mpenum: 0x18
   __TEXT.__swift5_protos: 0x1c
-  __TEXT.__unwind_info: 0x6b08
-  __TEXT.__eh_frame: 0xabd8
-  __DATA_CONST.__auth_got: 0x1b68
-  __DATA_CONST.__got: 0xc60
-  __DATA_CONST.__auth_ptr: 0x9e0
-  __DATA_CONST.__const: 0x148e0
+  __TEXT.__unwind_info: 0x6c90
+  __TEXT.__eh_frame: 0xae80
+  __DATA_CONST.__auth_got: 0x1ae8
+  __DATA_CONST.__got: 0xc58
+  __DATA_CONST.__auth_ptr: 0xa18
+  __DATA_CONST.__const: 0x14fd0
   __DATA_CONST.__cfstring: 0x6760
   __DATA_CONST.__objc_classlist: 0x550
   __DATA_CONST.__objc_catlist: 0xb8

   __DATA_CONST.__objc_dictobj: 0x50
   __DATA_CONST.__objc_intobj: 0x210
   __DATA_CONST.__objc_arrayobj: 0x30
-  __DATA.__objc_const: 0x1b7b0
-  __DATA.__objc_selrefs: 0x46c0
+  __DATA.__objc_const: 0x1b7c0
+  __DATA.__objc_selrefs: 0x46c8
   __DATA.__objc_ivar: 0x6e4
   __DATA.__objc_data: 0x4528
-  __DATA.__data: 0x6378
-  __DATA.__bss: 0xef50
-  __DATA.__common: 0xdc0
+  __DATA.__data: 0x63d8
+  __DATA.__bss: 0x10128
+  __DATA.__common: 0xdc8
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 9542
-  Symbols:   1480
-  CStrings:  6390
+  Functions: 9658
+  Symbols:   1465
+  CStrings:  6395
 
Symbols:
+ _$ss22KeyedDecodingContainerV6decode_6forKeyS2dm_xtKF
- _swift_taskGroup_wait_next_throwing
- _$s10Foundation4DateV9formattedSSyF
- _ftell
- _$sSa37_appendElementAssumeUniqueAndCapacity_03newB0ySi_xntFyXl_Ts5
- _rewind
- _fclose
- _$sSa034_makeUniqueAndReserveCapacityIfNotB0yyFyXl_Ts5
- _swift_unexpectedError
- _fseek
- _fread
- _$sSa16_createNewBuffer14bufferIsUnique15minimumCapacity13growForAppendySb_SiSbtFyXl_Ts5
- _fopen
- __availability_version_check
- _sscanf
- _dispatch_once_f
- _dlsym
CStrings:
+ "Failed to decode "
+ "Unsupported response content type: "
+ "Invalid external purchase token family entity "
+ "Requesting token "
+ "tokenEntries"
+ "Missing token family ID for "
+ ", will request new external purchase tokens"
+ " TEXT NOT NULL,\nPRIMARY KEY (\n"
+ "Clearing saved token family ID for bundleID: "
+ "application/x-apple-plist"
+ "DROP TABLE IF EXISTS external_gateway_tokens; DELETE FROM schema_version WHERE schema_name == 'storekit_external_purchase_tokens';"
+ "(ExternalPurchaseTokenV1UpdateResponse in _A0B67E5E835CE5C4351F500DE01F7FFD)"
+ "No Content-Type found in the response headers, cannot decode response"
+ "Failed to save token family id for "
+ "(ExternalPurchaseTokenV1Response in _A0B67E5E835CE5C4351F500DE01F7FFD)"
+ "hasActiveToken"
+ "external_gateway_token_families"
+ "Saving new token family ID for "
+ "tokenType"
+ "Using cached token family ID for "
+ "External purchase token update request failed for "
+ "BindPaymentAccountEligibilityResponse"
+ "_TtC9storekitdP33_A0B67E5E835CE5C4351F500DE01F7FFD32ExternalGatewayTokenFamilyEntity"
+ "externalPurchaseTokenV2Refresh"
+ " tokens found in response"
+ "tokenFamilyId"
+ "Sep 17 2024"
+ "17:40:33"
+ "storekit_external_purchase_token_families"
+ "cacheExpirationDate"
+ "(ExternalPurchaseTokenV2Response in _A0B67E5E835CE5C4351F500DE01F7FFD)"
+ "Expected empty response"
+ "Ignoring external purchase token update request for non-v1 token"
+ "No ExternalGatewayTokenFamily migration for "
+ " external purchase token request"
+ "_TtC9storekitdP33_A0B67E5E835CE5C4351F500DE01F7FFD31ExternalGatewayTokenFamilyStore"
- "CFDictionaryGetValue"
- "storekit_external_purchase_tokens"
- "Saving new token for mode "
- "23:41:45"
- "Response states there is an active token, but no token information was parsed"
- "/System/Library/CoreServices/SystemVersion.plist"
- "Using cached token for mode "
- "CFPropertyListCreateFromXMLData"
- "CFStringGetCString"
- "ProductVersion"
- "Clearing all external purchase tokens before "
- " INTEGER NOT NULL,\n"
- "external_gateway_tokens"
- "CFStringGetTypeID"
- "No ExternalGatewayTokens migration for "
- "Received external purchase token "
- "%!d(MISSING).%!d(MISSING).%!d(MISSING)"
- "r"
- "CFPropertyListCreateWithData"
- "Failed to save token ("
- "CFRelease"
- " DATETIME DEFAULT (timestamp()),\nPRIMARY KEY (\n"
- "Invalid external purchase token entity "
- "CFGetTypeID"
- "_TtC9storekitdP33_A0B67E5E835CE5C4351F500DE01F7FFD26ExternalGatewayTokenEntity"
- "_Concurrency/TaskGroup.swift"
- "CFDataCreateWithBytesNoCopy"
- "kCFAllocatorNull"
- "Error updating token status: "
- "_TtC9storekitdP33_A0B67E5E835CE5C4351F500DE01F7FFD25ExternalGatewayTokenStore"
- "Sep  2 2024"
- "CFStringCreateWithCStringNoCopy"

```
