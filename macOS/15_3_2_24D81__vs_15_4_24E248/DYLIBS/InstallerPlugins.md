## InstallerPlugins

> `/System/Library/Frameworks/InstallerPlugins.framework/Versions/A/InstallerPlugins`

```diff

 1301.0.0.0.0
-  __TEXT.__text: 0x9f04
+  __TEXT.__text: 0x9f28
   __TEXT.__auth_stubs: 0x340
-  __TEXT.__objc_methlist: 0xea4
+  __TEXT.__objc_methlist: 0x12e0
   __TEXT.__cstring: 0x9e1
   __TEXT.__gcc_except_tab: 0x1f8
   __TEXT.__const: 0x90

   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x12c0
+  __DATA_CONST.__objc_selrefs: 0x1500
   __DATA_CONST.__objc_superrefs: 0x78
   __DATA_CONST.__objc_arraydata: 0x8
   __AUTH_CONST.__auth_got: 0x1b0
   __AUTH_CONST.__const: 0x30
   __AUTH_CONST.__cfstring: 0xfa0
-  __AUTH_CONST.__objc_const: 0x3000
+  __AUTH_CONST.__objc_const: 0x27e8
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x550
   __DATA.__objc_ivar: 0x180

   - /System/Library/PrivateFrameworks/Install.framework/Versions/A/Install
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8066F6DD-00B8-39F3-B06C-0C199095FA85
-  Functions: 297
-  Symbols:   1221
+  UUID: 1100D779-980A-35E2-8299-0BCF88E9F4C6
+  Functions: 298
+  Symbols:   1222
   CStrings:  1256
 
Symbols:
+ -[IFXDebugMenu _addEnvironmentVariablesToMenu:].cold.1
Functions:
~ -[IAAutoSizedTextView drawRect:] : 200 -> 204
~ -[IFXOpaqueContentView drawRect:] : 112 -> 116
~ -[IFXDiskButtonCell setRepresentedObject:] : 1236 -> 1240
~ -[IFXDiskButtonCell drawInteriorWithFrame:inView:] : 1148 -> 1160
~ -[IFXDiskButtonCell(Private) _calculatePositions] : 980 -> 948
~ -[IFXDiskMatrixController _KVHandling:] : 272 -> 276
~ -[IFXLogDataSource setLogFilter:] : 84 -> 76
~ -[IFXLogDataSource(Private) _syncObjectsFromBuffer] : 620 -> 612
~ -[IFXFileListWindow backgroundThreadMethod] : 248 -> 252
~ -[IFXDebugMenu _addEnvironmentVariablesToMenu:] : 600 -> 564
~ -[IATextView menuForEvent:] : 80 -> 84
~ ___67+[NSImage(InstallerAdditions) selectionBarImageOfSize:isGrayscale:]_block_invoke : 172 -> 176
~ ___82+[IFXDocumentTools saveView:withDefaultFileName:modalForWindow:completionHandler:]_block_invoke : 620 -> 608

```
