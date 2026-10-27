## CPAnalytics

> `/System/Library/PrivateFrameworks/CPAnalytics.framework/Versions/A/CPAnalytics`

```diff

-911.0.134.0.0
-  __TEXT.__text: 0x138a4
-  __TEXT.__objc_methlist: 0x141c
+916.58.114.0.0
+  __TEXT.__text: 0x136a0
+  __TEXT.__objc_methlist: 0x1414
   __TEXT.__const: 0x188
   __TEXT.__gcc_except_tab: 0x174
-  __TEXT.__cstring: 0x259c
-  __TEXT.__oslogstring: 0xfe7
-  __TEXT.__unwind_info: 0x4f8
+  __TEXT.__cstring: 0x262e
+  __TEXT.__oslogstring: 0xf9d
+  __TEXT.__unwind_info: 0x4f0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x6d8
+  __DATA_CONST.__const: 0x6d0
   __DATA_CONST.__objc_classlist: 0xd8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xd90
+  __DATA_CONST.__objc_selrefs: 0xd80
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0xb0
   __DATA_CONST.__objc_arraydata: 0x60
-  __DATA_CONST.__got: 0x298
+  __DATA_CONST.__got: 0x290
   __AUTH_CONST.__const: 0x350
-  __AUTH_CONST.__cfstring: 0x2ca0
+  __AUTH_CONST.__cfstring: 0x2ce0
   __AUTH_CONST.__objc_const: 0x2620
   __AUTH_CONST.__objc_intobj: 0x3c0
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x128
-  __DATA.__data: 0x248
   __DATA.__bss: 0x19
   __DATA_DIRTY.__objc_data: 0x870
+  __DATA_DIRTY.__data: 0x248
   __DATA_DIRTY.__bss: 0x58
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftDemangle.dylib
-  Functions: 402
-  Symbols:   1500
-  CStrings:  458
+  Functions: 401
+  Symbols:   1495
+  CStrings:  459
 
Symbols:
+ GCC_except_table146
+ GCC_except_table152
+ GCC_except_table158
+ GCC_except_table189
+ GCC_except_table193
+ GCC_except_table197
+ GCC_except_table199
+ GCC_except_table383
- -[CPAnalyticsBiomeDestination _donatePhotoDeleteEventWithBaseSample:andEvent:]
- GCC_except_table147
- GCC_except_table156
- GCC_except_table159
- GCC_except_table190
- GCC_except_table194
- GCC_except_table198
- GCC_except_table200
- GCC_except_table384
- _CPAnalyticsPhotosDeleteKey
- _OBJC_CLASS_$_BMPhotosDelete
- _objc_msgSend$Delete
- _objc_msgSend$_donatePhotoDeleteEventWithBaseSample:andEvent:
Functions:
~ -[CPAnalyticsBiomeDestination _sendBiomeEvent:matcher:] : 868 -> 828
- -[CPAnalyticsBiomeDestination _donatePhotoDeleteEventWithBaseSample:andEvent:]
~ +[CPAnalyticsCoreAnalyticsHelper upgradePayload:sourceEvent:] : 680 -> 712
CStrings:
+ "com.apple.photos.CPAnalytics.gridHeaderControlTapped"
+ "com.apple.photos.CPAnalytics.slideshowCustomized"
+ "com.apple.photos.CPAnalytics.stagingArea.selectionCommitted"
- "/photos/deletes"
- "[Biome][Donation][Photos][Delete] Sent a photo delete event with uuid: %@"
```
