## WiFiAnalytics

> `/System/Library/PrivateFrameworks/WiFiAnalytics.framework/Versions/A/WiFiAnalytics`

```diff

-602.46.0.0.0
-  __TEXT.__text: 0xfa860
+602.44.0.0.0
+  __TEXT.__text: 0xf9f44
   __TEXT.__auth_stubs: 0xd70
-  __TEXT.__objc_methlist: 0xc224
-  __TEXT.__const: 0x2c0
-  __TEXT.__cstring: 0xdc3b
-  __TEXT.__oslogstring: 0xabfc
+  __TEXT.__objc_methlist: 0xc21c
+  __TEXT.__const: 0x2b0
+  __TEXT.__cstring: 0xda9c
+  __TEXT.__oslogstring: 0xa92f
   __TEXT.__swift5_typeref: 0x128
   __TEXT.__constg_swiftt: 0x178
   __TEXT.__swift5_reflstr: 0x61
   __TEXT.__swift5_fieldmd: 0x70
   __TEXT.__swift5_capture: 0x2c0
   __TEXT.__swift5_types: 0x4
-  __TEXT.__gcc_except_tab: 0x1080
+  __TEXT.__gcc_except_tab: 0x101c
   __TEXT.__unwind_info: 0x1cd8
   __TEXT.__eh_frame: 0x670
-  __TEXT.__objc_classname: 0xaaf
-  __TEXT.__objc_methname: 0x18efe
+  __TEXT.__objc_classname: 0xaae
+  __TEXT.__objc_methname: 0x18ef2
   __TEXT.__objc_methtype: 0x3487
-  __TEXT.__objc_stubs: 0x8cc0
+  __TEXT.__objc_stubs: 0x8ca0
   __DATA_CONST.__got: 0x628
-  __DATA_CONST.__const: 0xff8
+  __DATA_CONST.__const: 0xfd8
   __DATA_CONST.__objc_classlist: 0x2d8
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6b18
+  __DATA_CONST.__objc_selrefs: 0x6b10
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x238
   __DATA_CONST.__objc_arraydata: 0xf0
   __AUTH_CONST.__auth_got: 0x6c8
   __AUTH_CONST.__auth_ptr: 0x30
-  __AUTH_CONST.__const: 0x1d30
-  __AUTH_CONST.__cfstring: 0xafc0
+  __AUTH_CONST.__const: 0x1d10
+  __AUTH_CONST.__cfstring: 0xafa0
   __AUTH_CONST.__objc_const: 0x10d68
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_arrayobj: 0x180

   __DATA.__bss: 0x18
   __DATA.__common: 0x11e8
   __DATA_DIRTY.__objc_data: 0x320
-  __DATA_DIRTY.__bss: 0xa8
+  __DATA_DIRTY.__bss: 0x88
   __DATA_DIRTY.__common: 0x10
   - /System/Library/Frameworks/CoreData.framework/Versions/A/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 4609
-  Symbols:   7867
-  CStrings:  2081
+  Functions: 4605
+  Symbols:   7858
+  CStrings:  2073
 
Symbols:
+ +[AnalyticsStoreMOContext sharedWAPersistenceCoordinator:]
+ ___58+[AnalyticsStoreMOContext sharedWAPersistenceCoordinator:]_block_invoke
+ _objc_msgSend$sharedWAPersistenceCoordinator:
- +[AnalyticsStoreMOContext sharedManagedObjectModel:]
- +[AnalyticsStoreMOHandler isStoreCompatible]
- ___43+[AnalyticsStoreDescriptor defaultModelURL]_block_invoke
- ___52+[AnalyticsStoreMOContext sharedManagedObjectModel:]_block_invoke
- ___53+[AnalyticsStoreDescriptor defaultPersistentStoreURL]_block_invoke
- ___64+[AnalyticsPersistenceManager isStoreCompatibleAtURL:withModel:]_block_invoke
- ___block_descriptor_40_e5_v8?0l
- _objc_msgSend$isStoreCompatible
- _objc_msgSend$sharedManagedObjectModel:
CStrings:
+ "+[AnalyticsStoreMOContext sharedWAPersistenceCoordinator:]_block_invoke"
- "+[AnalyticsPersistenceManager isStoreCompatibleAtURL:withModel:]"
- "+[AnalyticsPersistenceManager isStoreCompatibleAtURL:withModel:]_block_invoke"
- "+[AnalyticsProcessor sharedAnalyticsProcessor]"
- "+[AnalyticsStoreDescriptor defaultModelURL]"
- "+[AnalyticsStoreDescriptor defaultModelURL]_block_invoke"
- "+[AnalyticsStoreDescriptor defaultPersistentStoreURL]_block_invoke"
- "+[AnalyticsStoreMOContext sharedManagedObjectModel:]_block_invoke"
- "+[AnalyticsStoreMOHandler isStoreCompatible]"
- "isStoreCompatible"

```
