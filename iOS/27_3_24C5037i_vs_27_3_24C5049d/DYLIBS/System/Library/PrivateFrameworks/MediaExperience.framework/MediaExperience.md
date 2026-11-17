## MediaExperience

> `/System/Library/PrivateFrameworks/MediaExperience.framework/MediaExperience`

```diff

-390.6.1.0.0
-  __TEXT.__text: 0x257ad4
+390.9.1.0.0
+  __TEXT.__text: 0x257e14
   __TEXT.__delay_helper: 0x304
   __TEXT.__lazy_helpers: 0xfc
-  __TEXT.__objc_methlist: 0x8d80
-  __TEXT.__cstring: 0x39f51
+  __TEXT.__objc_methlist: 0x8da8
+  __TEXT.__cstring: 0x39fc6
   __TEXT.__const: 0x1d40
   __TEXT.__gcc_except_tab: 0x5068
-  __TEXT.__oslogstring: 0x533cf
+  __TEXT.__oslogstring: 0x53432
   __TEXT.__dlopen_cstrs: 0x613
-  __TEXT.__unwind_info: 0x82c0
+  __TEXT.__unwind_info: 0x82c8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x7438
+  __DATA_CONST.__const: 0x7440
   __DATA_CONST.__objc_classlist: 0x348
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5750
+  __DATA_CONST.__objc_selrefs: 0x5768
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x318
   __DATA_CONST.__objc_arraydata: 0xf8
   __DATA_CONST.__got: 0xd58
   __AUTH_CONST.__const: 0x4ac8
-  __AUTH_CONST.__cfstring: 0x1c7e0
-  __AUTH_CONST.__objc_const: 0xd9c8
+  __AUTH_CONST.__cfstring: 0x1c860
+  __AUTH_CONST.__objc_const: 0xda08
   __AUTH_CONST.__weak_auth_got: 0x18
   __AUTH_CONST.__lazy_load_got: 0x10
   __AUTH_CONST.__objc_arrayobj: 0x78

   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x19a0
   __AUTH.__data: 0x630
-  __DATA.__objc_ivar: 0xd1c
+  __DATA.__objc_ivar: 0xd20
   __DATA.__data: 0x1450
   __DATA.__common: 0x5d0
   __DATA_DIRTY.__objc_data: 0x730
-  __DATA_DIRTY.__bss: 0xd00
+  __DATA_DIRTY.__bss: 0xd10
   __DATA_DIRTY.__common: 0x60
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CoreAudio.framework/CoreAudio

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 10310
-  Symbols:   13809
-  CStrings:  10137
+  Functions: 10316
+  Symbols:   13814
+  CStrings:  10142
 
Symbols:
+ -[MXSessionManager(Utilities) isEndInterruptionLikelyToBeResumableForInterruptor:victim:]
+ -[MXSystemController canQueryRecordingClients]
+ -[MXSystemController hasEntitlementToQueryRecordingClients]
+ -[MXSystemController setHasEntitlementToQueryRecordingClients:]
+ GCC_except_table110
+ GCC_except_table126
+ GCC_except_table147
+ _OBJC_IVAR_$_MXSystemController._hasEntitlementToQueryRecordingClients
+ ___mxsvlFormatTimestamp_block_invoke
+ _gMXSystemControllerRecordingClientsProperties
+ _kMXSessionInterruptionInfoKey_EndInterruptionLikelyToBeResumable
+ _mxsvlCopyRouteEntry
+ _mxsvlFormatTimestamp.onceToken
+ _mxsvlFormatTimestamp.sTimestampFormatter
- GCC_except_table120
- GCC_except_table122
- GCC_except_table146
- GCC_except_table28
- ___mxsvlGetTimestampFormatter_block_invoke
- _mxsvlGetNewestOperationDate
- _mxsvlGetTimestampFormatter.onceToken
- _mxsvlGetTimestampFormatter.sTimestampFormatter
- _setAttributeForKeyInternal:andValue:.onceToken
CStrings:
+ "-MXSystemController- %s: Client %{public}@/%d does not have entitlement to subscribe to %{public}@"
+ "Categories"
+ "EndInterruptionLikelyToBeResumable"
+ "LastUsed"
+ "com.apple.private.mediaexperience.queryrecordingclients.allow"
```
