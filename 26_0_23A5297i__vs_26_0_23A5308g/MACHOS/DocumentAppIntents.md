## DocumentAppIntents

> `/System/Library/ExtensionKit/Extensions/DocumentAppIntents.appex/DocumentAppIntents`

```diff

-364.0.0.0.0
-  __TEXT.__text: 0x561e6c
-  __TEXT.__auth_stubs: 0x8920
+366.0.0.0.0
+  __TEXT.__text: 0x5660d8
+  __TEXT.__auth_stubs: 0x8940
   __TEXT.__objc_stubs: 0x74e0
-  __TEXT.__objc_methlist: 0xcd4c
-  __TEXT.__const: 0x19948
-  __TEXT.__objc_methname: 0x1e80b
-  __TEXT.__cstring: 0x32f81
-  __TEXT.__oslogstring: 0xecbd
+  __TEXT.__objc_methlist: 0xcd3c
+  __TEXT.__const: 0x198f8
+  __TEXT.__objc_methname: 0x1e80a
+  __TEXT.__cstring: 0x331f1
+  __TEXT.__oslogstring: 0xeefd
   __TEXT.__objc_classname: 0xf8d
-  __TEXT.__objc_methtype: 0x6bc7
+  __TEXT.__objc_methtype: 0x6bfc
   __TEXT.__gcc_except_tab: 0x5cc
   __TEXT.__ustring: 0x10
-  __TEXT.__swift5_typeref: 0x11eaa
-  __TEXT.__constg_swiftt: 0x172f8
-  __TEXT.__swift5_reflstr: 0xf0ac
-  __TEXT.__swift5_fieldmd: 0xc218
+  __TEXT.__swift5_typeref: 0x12168
+  __TEXT.__constg_swiftt: 0x172cc
+  __TEXT.__swift5_reflstr: 0xf08c
+  __TEXT.__swift5_fieldmd: 0xc1cc
   __TEXT.__swift5_builtin: 0x7d0
   __TEXT.__swift5_assocty: 0x14e0
   __TEXT.__swift5_proto: 0xf1c
-  __TEXT.__swift5_types: 0xc78
+  __TEXT.__swift5_types: 0xc74
   __TEXT.__swift5_capture: 0xcf7c
   __TEXT.__swift_as_entry: 0x1c0
   __TEXT.__swift_as_ret: 0x220
   __TEXT.__swift5_protos: 0x184
   __TEXT.__swift5_mpenum: 0x84
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0xdf40
+  __TEXT.__unwind_info: 0xdf38
   __TEXT.__eh_frame: 0x7d48
-  __DATA_CONST.__auth_got: 0x44a0
-  __DATA_CONST.__got: 0x2600
+  __DATA_CONST.__auth_got: 0x44b0
+  __DATA_CONST.__got: 0x25f8
   __DATA_CONST.__auth_ptr: 0x2a78
-  __DATA_CONST.__const: 0x2d180
+  __DATA_CONST.__const: 0x2d178
   __DATA_CONST.__cfstring: 0xb40
   __DATA_CONST.__objc_classlist: 0xc88
   __DATA_CONST.__objc_catlist: 0xf0

   __DATA_CONST.__objc_arraydata: 0x70
   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0x22a30
-  __DATA.__objc_selrefs: 0x8058
+  __DATA.__objc_const: 0x229f0
+  __DATA.__objc_selrefs: 0x8060
   __DATA.__objc_ivar: 0x214
-  __DATA.__objc_data: 0x1b220
-  __DATA.__data: 0x1a3d8
+  __DATA.__objc_data: 0x1b1e8
+  __DATA.__data: 0x1a388
   __DATA.__objc_stublist: 0x20
   __DATA.__bss: 0x1a558
-  __DATA.__common: 0xb10
+  __DATA.__common: 0xb18
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/AppIntents.framework/AppIntents
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 2D87CD8A-66A5-3F0D-88E2-5E48D8CE7EFF
-  Functions: 22498
-  Symbols:   1335
-  CStrings:  11035
+  UUID: D5F8B761-A124-388A-8433-4413D408426B
+  Functions: 22499
+  Symbols:   1333
+  CStrings:  11065
 
Symbols:
+ _objc_retain_x13
- _CGRectIntersectsRect
- _UIKeyboardAnimationCurveUserInfoKey
- _UIKeyboardAnimationDurationUserInfoKey
CStrings:
+ "%s Failed to unarchive a node from teamData: %s. Continue by trying to unarchive data representation from item provider"
+ "%s Unarchived a node from teamData: %s"
+ "%s itemProvider: %s teamData: %s"
+ "%s, encoded teamData: %s for node: %s"
+ "%s, failed to encode node for teamData error: %s"
+ "%s: %s, failed to register NSUserActivity for folder. Error: %s"
+ "0 size for outline sizes could cause resize issues %s"
+ "?"
+ "@\"<DOCNode>\""
+ "@\"FPItem\""
+ "@\"UIDocumentBrowserAction\""
+ "@\"UIScrollView\""
+ "@\"UITextField\""
+ "@\"_TtC18DocumentAppIntents15DOCFilenameView\""
+ "@\"_TtC18DocumentAppIntents19DOCSearchController\""
+ "@\"_TtC18DocumentAppIntents28DOCItemCollectionCellContent\""
+ "@\"_TtC18DocumentAppIntents31DOCItemCollectionViewController\""
+ "@\"_TtC18DocumentAppIntents33DOCBrowserContainedViewController\""
+ "@\"_TtCC18DocumentAppIntents18DOCDocumentManager23DocumentCreationSession\""
+ "DOCBrowserHistoryDataSource.clearHistoryNotification"
+ "DOCFileSystemCollectionManager: Application did enter Background, Stopping %ld active collections"
+ "DOCNodeCollectionDelegate flat nodes %s"
+ "Title for the action to unfavorite a folder"
+ "_collectionView:typeSelectResultDidUpdate:"
+ "clearHistoryObserverToken"
+ "compactProgressButtonItem"
+ "d"
+ "expandedChildNodesMap"
+ "ignoring snapshot update because of invalid nodes"
+ "priority"
+ "registerNode(_:supportsPickingFolders:disableExternalFolders:includeTeamDataForPasteboard:)"
+ "regularProgressButtonItem"
+ "setLeftBarButtonItems:animated:"
+ "teamData"
+ "v32@0:8@\"UICollectionView\"16@\"_UITypeSelectResult\"24"
+ "{NSDirectionalEdgeInsets=dddd}"
- "%@: %@, failed to regsiter NSUserActivity for folder"
- "DOCFileSystemCollectionManager: Application did enter Background, Stoping %ld active collections"
- "Title for the action to unfavortie a folder"
- "circle.grid.2x2.topleft.checkmark.filled"
- "convertRect:fromWindow:"
- "flipsHorizontallyInOppositeLayoutDirection"
- "folderCustomizationEnabled"
- "mapofnodes"
- "oldContentOffset"
- "progressButtonItem"
- "registerNode(_:supportsPickingFolders:disableExternalFolders:)"
- "widthConstraint"

```
