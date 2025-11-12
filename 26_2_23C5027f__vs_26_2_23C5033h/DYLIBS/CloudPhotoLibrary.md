## CloudPhotoLibrary

> `/System/Library/PrivateFrameworks/CloudPhotoLibrary.framework/CloudPhotoLibrary`

```diff

-820.0.140.0.0
-  __TEXT.__text: 0x199204
+820.0.170.0.0
+  __TEXT.__text: 0x199228
   __TEXT.__auth_stubs: 0xf00
   __TEXT.__objc_methlist: 0x13134
   __TEXT.__const: 0x300

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcupolicy.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A160F401-D4F3-3D2B-8634-F74EC332144C
+  UUID: 84236295-4963-3096-946D-3688AB4F4C0E
   Functions: 8492
-  Symbols:   26233
+  Symbols:   26234
   CStrings:  14887
 
Symbols:
+ ___chkstk_darwin
Functions:
~ +[CPLExpungeableResourceState normalizedExpungeableResourceStatesFromExpungeableResourceStates:] : 680 -> 700
~ +[CPLResource normalizedResourcesFromResources:resourcePerResourceType:] : 716 -> 736
~ -[CPLProxyLibraryManager noteClientReceivedNotificationOfServerChanges] : 108 -> 104
CStrings:
+ "CloudPhotoLibrary-820.0.170"
- "CloudPhotoLibrary-820.0.140"

```
