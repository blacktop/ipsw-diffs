## AccessoryMediaLibrary

> `/System/Library/PrivateFrameworks/AccessoryMediaLibrary.framework/AccessoryMediaLibrary`

```diff

-  __TEXT.__text: 0x14164
+  __TEXT.__text: 0x14570
   __TEXT.__objc_methlist: 0x1364
   __TEXT.__const: 0x100
-  __TEXT.__oslogstring: 0x2220
+  __TEXT.__oslogstring: 0x237e
   __TEXT.__cstring: 0xcaa
-  __TEXT.__gcc_except_tab: 0x1b0
+  __TEXT.__gcc_except_tab: 0x1ac
   __TEXT.__unwind_info: 0x4b0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa38
+  __DATA_CONST.__objc_selrefs: 0xa40
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x50
   __DATA_CONST.__got: 0x88

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 470
-  Symbols:   1785
-  CStrings:  283
+  Functions: 472
+  Symbols:   1797
+  CStrings:  287
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__const : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__got : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH.__objc_data : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__data : content changed
Symbols:
+ GCC_except_table61
+ ___59-[AccessoryMediaLibraryClient availableLibrariesDidChange:]_block_invoke
+ _objc_msgSend$isEqualToArray:
- GCC_except_table60
- _objc_msgSend$setMockListenerEndpoint:
Functions:
~ ___56-[AccessoryMediaLibraryClient _performWithRemoteObject:]_block_invoke : 144 -> 248
~ -[AccessoryMediaLibraryClient requestLibraryInfoUpdate:] : 292 -> 184
~ ___56-[AccessoryMediaLibraryClient requestLibraryInfoUpdate:]_block_invoke : 16 -> 152
~ -[AccessoryMediaLibraryClient confirmUpdate:library:lastRevision:updateCount:] : 240 -> 420
~ -[AccessoryMediaLibraryClient availableLibrariesDidChange:] : 480 -> 324
+ ___59-[AccessoryMediaLibraryClient availableLibrariesDidChange:]_block_invoke
~ -[AccessoryMediaLibraryClient setMockListenerEndpoint:] : 12 -> 88
~ _OUTLINED_FUNCTION_3 : 28 -> 12
~ -[ACCMediaLibraryAccessory confirmUpdates:revision:count:] : 616 -> 612
~ ___58-[ACCMediaLibraryAccessory confirmUpdates:revision:count:]_block_invoke : 1792 -> 2036
~ -[ACCMediaLibraryAccessory confirmPlaylistContentUpdates:revision:] : 436 -> 432
~ ___74-[ACCMediaLibraryProvider confirmUpdate:library:lastRevision:updateCount:]_block_invoke : 1148 -> 1140
~ ___77-[ACCMediaLibraryProvider confirmPlaylistContentUpdate:library:lastRevision:]_block_invoke : 860 -> 856
+ ___56-[AccessoryMediaLibraryClient _performWithRemoteObject:]_block_invoke.cold.2
~ ___55-[AccessoryMediaLibraryClient _connectToServiceOnQueue]_block_invoke.98.cold.2 : 60 -> 68
~ ___55-[AccessoryMediaLibraryClient _connectToServiceOnQueue]_block_invoke.100.cold.2 : 60 -> 68
~ ___66-[AccessoryMediaLibraryClient accessoryAttached:windowPerLibrary:]_block_invoke.cold.3 : 64 -> 72
~ ___logObjectForModule_block_invoke.cold.1 : 108 -> 104
CStrings:
+ "MediaLibrary XPC remoteObject unavailable; dropping outbound call to feature service (confirm/update may be lost)"
+ "availableLibrariesDidChange unchanged — coalescing"
+ "confirmUpdate: relaying to feature service accessory=%@ library=%@ lastRevision=%@ updateCount=%u"
+ "confirmUpdates: %@, library %@, revision %@, drained %lu update(s), waitlist now %lu"

```
