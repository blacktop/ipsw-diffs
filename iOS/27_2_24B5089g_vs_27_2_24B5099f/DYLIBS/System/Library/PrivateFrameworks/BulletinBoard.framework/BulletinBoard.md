## BulletinBoard

> `/System/Library/PrivateFrameworks/BulletinBoard.framework/BulletinBoard`

```diff

-955.2.1.0.0
-  __TEXT.__text: 0x7b600
-  __TEXT.__objc_methlist: 0x87dc
+955.2.2.0.0
+  __TEXT.__text: 0x7b778
+  __TEXT.__objc_methlist: 0x87e4
   __TEXT.__const: 0x1c0
   __TEXT.__cstring: 0x6d92
   __TEXT.__gcc_except_tab: 0x9b8
-  __TEXT.__oslogstring: 0x68a6
+  __TEXT.__oslogstring: 0x68c9
   __TEXT.__dlopen_cstrs: 0x19c
   __TEXT.__unwind_info: 0x2c38
   __TEXT.__objc_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x130
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x40f0
+  __DATA_CONST.__objc_selrefs: 0x40f8
   __DATA_CONST.__objc_protorefs: 0x68
   __DATA_CONST.__objc_superrefs: 0x210
   __DATA_CONST.__objc_arraydata: 0x190

   __AUTH_CONST.__objc_intobj: 0x108
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x8d4
   __DATA.__data: 0xe60
-  __DATA_DIRTY.__objc_data: 0x18b0
+  __DATA_DIRTY.__objc_data: 0x1900
   __DATA_DIRTY.__data: 0x14
-  __DATA_DIRTY.__bss: 0x1a8
+  __DATA_DIRTY.__bss: 0x1c8
   __DATA_DIRTY.__common: 0x70
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3415
-  Symbols:   5261
+  Functions: 3416
+  Symbols:   5262
   CStrings:  1545
 
Symbols:
+ -[BBSectionInfo _applyDestinationCapabilities:]
+ -[BBServer _copySectionSettingsFromSectionID:toSectionID:destinationCapabilities:]
+ -[BBServer copySectionSettingsFromSectionID:toSectionID:destinationCapabilities:withHandler:]
+ -[BBSettingsGateway copySectionSettingsFromSectionID:toSectionID:destinationCapabilities:withCompletion:]
+ ___105-[BBSettingsGateway copySectionSettingsFromSectionID:toSectionID:destinationCapabilities:withCompletion:]_block_invoke
+ ___105-[BBSettingsGateway copySectionSettingsFromSectionID:toSectionID:destinationCapabilities:withCompletion:]_block_invoke_2
+ ___93-[BBServer copySectionSettingsFromSectionID:toSectionID:destinationCapabilities:withHandler:]_block_invoke
- -[BBServer _copySectionSettingsFromSectionID:toSectionID:]
- -[BBServer copySectionSettingsFromSectionID:toSectionID:withHandler:]
- -[BBSettingsGateway copySectionSettingsFromSectionID:toSectionID:withCompletion:]
- ___69-[BBServer copySectionSettingsFromSectionID:toSectionID:withHandler:]_block_invoke
- ___81-[BBSettingsGateway copySectionSettingsFromSectionID:toSectionID:withCompletion:]_block_invoke
- ___81-[BBSettingsGateway copySectionSettingsFromSectionID:toSectionID:withCompletion:]_block_invoke_2
CStrings:
+ "Copying section settings from %{public}@ to %{public}@ [ destinationCapabilities: 0x%lx ]"
- "Copying section settings from %{public}@ to %{public}@"
```
