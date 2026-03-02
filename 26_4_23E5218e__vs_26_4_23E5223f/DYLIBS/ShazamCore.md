## ShazamCore

> `/System/Library/PrivateFrameworks/ShazamCore.framework/ShazamCore`

```diff

-426.4.35.1.0
-  __TEXT.__text: 0x16c2c
+426.4.38.0.0
+  __TEXT.__text: 0x172dc
   __TEXT.__auth_stubs: 0xcd0
-  __TEXT.__objc_methlist: 0x1334
+  __TEXT.__objc_methlist: 0x136c
   __TEXT.__const: 0x1454
-  __TEXT.__gcc_except_tab: 0x198
-  __TEXT.__oslogstring: 0x8c3
+  __TEXT.__gcc_except_tab: 0x1a4
+  __TEXT.__oslogstring: 0xaa3
   __TEXT.__cstring: 0x1102
   __TEXT.__swift5_typeref: 0x3b2
   __TEXT.__swift5_capture: 0x5c

   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_proto: 0x128
   __TEXT.__swift5_types: 0x54
-  __TEXT.__unwind_info: 0x8c0
+  __TEXT.__unwind_info: 0x8d8
   __TEXT.__eh_frame: 0x688
   __TEXT.__objc_classname: 0x34e
-  __TEXT.__objc_methname: 0x32e3
+  __TEXT.__objc_methname: 0x338e
   __TEXT.__objc_methtype: 0x75c
-  __TEXT.__objc_stubs: 0x2400
+  __TEXT.__objc_stubs: 0x24e0
   __DATA_CONST.__got: 0x2e8
-  __DATA_CONST.__const: 0x6b8
+  __DATA_CONST.__const: 0x6d8
   __DATA_CONST.__objc_classlist: 0x128
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xcc8
+  __DATA_CONST.__objc_selrefs: 0xd00
   __DATA_CONST.__objc_superrefs: 0xe0
   __AUTH_CONST.__auth_got: 0x678
-  __AUTH_CONST.__const: 0xbe8
+  __AUTH_CONST.__const: 0xc08
   __AUTH_CONST.__cfstring: 0x12a0
   __AUTH_CONST.__objc_const: 0x2930
   __AUTH.__objc_data: 0x9d0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 712F25BD-90E8-3A88-B9E8-36009867F758
-  Functions: 746
-  Symbols:   1882
-  CStrings:  1064
+  UUID: 3586B889-922D-3D1C-95CC-0AC4845C9B47
+  Functions: 753
+  Symbols:   1905
+  CStrings:  1078
 
Symbols:
+ -[SHMusicalFeaturesBagConfiguration setAmsPromise:]
+ -[SHMusicalFeaturesBagConfiguration setConfiguration:]
+ -[SHRemoteConfiguration cachedDictionaryForKey:]
+ -[SHRemoteConfiguration cachedMusicalFeaturesBagConfiguration]
+ -[SHRemoteConfiguration cachedRematchBagConfiguration]
+ ___48-[SHRemoteConfiguration cachedDictionaryForKey:]_block_invoke
+ ___53-[SHMusicalFeaturesBagConfiguration initWithPromise:]_block_invoke.11
+ ___block_descriptor_32_e22_v16?0"NSDictionary"8l
+ ___block_literal_global.81
+ _objc_msgSend$cachedDictionaryForKey:
+ _objc_msgSend$cachedMusicalFeaturesBagConfiguration
+ _objc_msgSend$cachedRematchBagConfiguration
+ _objc_msgSend$cachedValuesForKeys:observationToken:updateHandler:
+ _objc_msgSend$removeObserverWithToken:
+ _objc_msgSend$setWithObject:
+ _objc_msgSend$uninitializedToken
CStrings:
+ "Failed to load musical features bag configuration: %@"
+ "GET"
+ "Musical features bag configuration loaded successfully"
+ "Musical features bag value already loaded, using promise"
+ "Musical features bag value not loaded and no cache available, using promise"
+ "Musical features bag value not loaded, using cached configuration"
+ "Rematch bag value already loaded, using promise"
+ "Rematch bag value not loaded and no cache available, using promise"
+ "Rematch bag value not loaded, using cached configuration"
+ "cachedDictionaryForKey:"
+ "cachedMusicalFeaturesBagConfiguration"
+ "cachedRematchBagConfiguration"
+ "cachedValuesForKeys:observationToken:updateHandler:"
+ "removeObserverWithToken:"
+ "setWithObject:"
+ "uninitializedToken"
- "POST"
- "T@\"AMSPromise\",R,N,V_amsPromise"

```
