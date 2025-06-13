## VideoSubscriberAccount

> `/System/Library/Frameworks/VideoSubscriberAccount.framework/VideoSubscriberAccount`

```diff

-511.1.1.0.0
-  __TEXT.__text: 0xaf480
+511.10.14.0.0
+  __TEXT.__text: 0xaf9fc
   __TEXT.__auth_stubs: 0xf50
-  __TEXT.__objc_methlist: 0x7aac
+  __TEXT.__objc_methlist: 0x7af4
   __TEXT.__const: 0xe2f0
-  __TEXT.__cstring: 0x98f6
-  __TEXT.__oslogstring: 0x58be
+  __TEXT.__cstring: 0x9976
+  __TEXT.__oslogstring: 0x59a1
   __TEXT.__gcc_except_tab: 0x1224
   __TEXT.__ustring: 0x178
   __TEXT.__swift5_typeref: 0xe0

   __TEXT.__unwind_info: 0x23bc
   __TEXT.__eh_frame: 0x178
   __TEXT.__objc_classname: 0x12c7
-  __TEXT.__objc_methname: 0x1212c
+  __TEXT.__objc_methname: 0x122ba
   __TEXT.__objc_methtype: 0x1b19
-  __TEXT.__objc_stubs: 0xbcc0
+  __TEXT.__objc_stubs: 0xbdc0
   __DATA_CONST.__got: 0x360
-  __DATA_CONST.__const: 0x2930
+  __DATA_CONST.__const: 0x2980
   __DATA_CONST.__objc_classlist: 0x510
   __DATA_CONST.__objc_catlist: 0x98
   __DATA_CONST.__objc_protolist: 0x120
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x135c0
-  __DATA_CONST.__objc_selrefs: 0x3f10
+  __DATA_CONST.__objc_const: 0x13660
+  __DATA_CONST.__objc_selrefs: 0x3f58
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__cfstring: 0x8020
+  __AUTH_CONST.__cfstring: 0x80e0
   __AUTH_CONST.__objc_intobj: 0x1f8
   __AUTH_CONST.__objc_const: 0x0
-  __AUTH_CONST.__const: 0x4b50
+  __AUTH_CONST.__const: 0x4bd0
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_got: 0x7b8
   __AUTH.__data: 0x98
   __DATA.__objc_protorefs: 0x50
   __DATA.__objc_classrefs: 0x6a0
   __DATA.__objc_superrefs: 0x3d8
-  __DATA.__objc_ivar: 0x8ec
+  __DATA.__objc_ivar: 0x8f4
   __DATA.__data: 0x1a78
   __DATA.__bss: 0x800
   __DATA.__common: 0x44
-  __DATA_DIRTY.__const: 0xd60
+  __DATA_DIRTY.__const: 0xd00
   __DATA_DIRTY.__objc_const: 0x4410
   __DATA_DIRTY.__objc_data: 0x3250
   __DATA_DIRTY.__data: 0xc0

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  UUID: 83907703-294A-3E17-952D-505EB09F906E
-  Functions: 3696
-  Symbols:   11790
-  CStrings:  6266
+  UUID: 1A86193D-220D-3CF2-B508-465CD65E4CAD
+  Functions: 3703
+  Symbols:   11816
+  CStrings:  6295
 
Symbols:
+ -[VSDevice bincompatOS]
+ -[VSDevice bincompatPlatform]
+ -[VSIdentityProvider requireAuthenticationURLSystemTrust]
+ -[VSIdentityProvider requireXHRRequestSystemTrust]
+ -[VSIdentityProvider setRequireAuthenticationURLSystemTrust:]
+ -[VSIdentityProvider setRequireXHRRequestSystemTrust:]
+ GCC_except_table31
+ GCC_except_table44
+ _OBJC_IVAR_$_VSIdentityProvider._requireAuthenticationURLSystemTrust
+ _OBJC_IVAR_$_VSIdentityProvider._requireXHRRequestSystemTrust
+ ___24-[VSDevice serialNumber]_block_invoke.149
+ ___38-[VSDevice setIgnoreSetTopBoxProfile:]_block_invoke.135
+ ___38-[VSDevice setIgnoreSetTopBoxProfile:]_block_invoke.136
+ ___38-[VSDevice setIgnoreSetTopBoxProfile:]_block_invoke.136.cold.1
+ ___38-[VSDevice setIgnoreSetTopBoxProfile:]_block_invoke.140
+ ___38-[VSDevice setIgnoreSetTopBoxProfile:]_block_invoke.140.cold.1
+ ___48-[VSAccountChannelsCenter _saveAccountChannels:]_block_invoke.42
+ ___48-[VSAccountChannelsCenter _saveAccountChannels:]_block_invoke_2
+ ___69-[VSAccountChannelsCenter fetchAccountChannelsWithCompletionHandler:]_block_invoke.56
+ ___69-[VSAccountChannelsCenter fetchAccountChannelsWithCompletionHandler:]_block_invoke.58
+ ___69-[VSAccountChannelsCenter fetchAccountChannelsWithCompletionHandler:]_block_invoke.58.cold.1
+ ___69-[VSAccountChannelsCenter fetchAccountChannelsWithCompletionHandler:]_block_invoke.59
+ ___block_descriptor_32_e20_v20?0B8"NSError"12l
+ ___block_descriptor_73_e8_32s40s48s56s64bs_e40_v24?0"VSSetTopBoxProfile"8"NSError"16ls32l8s64l8s40l8s48l8s56l8
+ ___block_literal_global.134
+ ___block_literal_global.138
+ ___block_literal_global.142
+ ___block_literal_global.45
+ _objc_msgSend$bincompatPlatform
+ _objc_msgSend$requireAuthenticationURLSystemTrust
+ _objc_msgSend$requireBootUrlSystemTrust
+ _objc_msgSend$requireXHRRequestSystemTrust
+ _objc_msgSend$setBincompatDeviceFamily:
+ _objc_msgSend$setRequireAuthenticationURLSystemTrust:
+ _objc_msgSend$setRequireBootUrlSystemTrust:
+ _objc_msgSend$setRequireXHRRequestSystemTrust:
- GCC_except_table30
- GCC_except_table42
- ___24-[VSDevice serialNumber]_block_invoke.146
- ___38-[VSDevice setIgnoreSetTopBoxProfile:]_block_invoke.132
- ___38-[VSDevice setIgnoreSetTopBoxProfile:]_block_invoke.133
- ___38-[VSDevice setIgnoreSetTopBoxProfile:]_block_invoke.133.cold.1
- ___38-[VSDevice setIgnoreSetTopBoxProfile:]_block_invoke.137
- ___38-[VSDevice setIgnoreSetTopBoxProfile:]_block_invoke.137.cold.1
- ___48-[VSAccountChannelsCenter _saveAccountChannels:]_block_invoke.38
- ___69-[VSAccountChannelsCenter fetchAccountChannelsWithCompletionHandler:]_block_invoke.50
- ___69-[VSAccountChannelsCenter fetchAccountChannelsWithCompletionHandler:]_block_invoke.50.cold.1
- ___69-[VSAccountChannelsCenter fetchAccountChannelsWithCompletionHandler:]_block_invoke.51
- ___69-[VSAccountChannelsCenter fetchAccountChannelsWithCompletionHandler:]_block_invoke.52
- ___block_descriptor_65_e8_32s40s48s56bs_e40_v24?0"VSSetTopBoxProfile"8"NSError"16ls32l8s56l8s40l8s48l8
- ___block_literal_global.131
- ___block_literal_global.135
- ___block_literal_global.139
CStrings:
+ "\x01/\x03"
+ "RealityDevice"
+ "Recording Now Playing Broken event with data %@"
+ "Recording federated punchout event with data %@"
+ "TB,N,V_requireAuthenticationURLSystemTrust"
+ "TB,N,V_requireXHRRequestSystemTrust"
+ "Unable to fetch accounts from account store - fallback to local accounts."
+ "VSAccountChannels save to keychain: success %d, error %@"
+ "_requireAuthenticationURLSystemTrust"
+ "_requireXHRRequestSystemTrust"
+ "bincompatOS"
+ "bincompatPlatform"
+ "realityDevice"
+ "requireAuthenticationURLSystemTrust"
+ "requireBootUrlSystemTrust"
+ "requireXHRRequestSystemTrust"
+ "setBincompatDeviceFamily:"
+ "setRequireAuthenticationURLSystemTrust:"
+ "setRequireBootUrlSystemTrust:"
+ "setRequireXHRRequestSystemTrust:"
+ "xros"
- "\x01\x1f\x03"

```
