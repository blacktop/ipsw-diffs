## WelcomeKitUI

> `/System/Library/PrivateFrameworks/WelcomeKitUI.framework/WelcomeKitUI`

```diff

-1439.0.0.0.0
-  __TEXT.__text: 0x13d14
-  __TEXT.__objc_methlist: 0x1ae4
-  __TEXT.__const: 0x92
-  __TEXT.__cstring: 0x4ec0
+1441.40.1.0.0
+  __TEXT.__text: 0x142dc
+  __TEXT.__objc_methlist: 0x1b7c
+  __TEXT.__const: 0x9a
+  __TEXT.__cstring: 0x4fd0
   __TEXT.__gcc_except_tab: 0x2ac
   __TEXT.__constg_swiftt: 0x38
   __TEXT.__swift5_typeref: 0x14
   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x728
+  __TEXT.__unwind_info: 0x760
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x588
+  __DATA_CONST.__const: 0x5b0
   __DATA_CONST.__objc_classlist: 0x140
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1458
+  __DATA_CONST.__objc_selrefs: 0x14d0
   __DATA_CONST.__objc_superrefs: 0x108
   __DATA_CONST.__objc_arraydata: 0xb68
-  __DATA_CONST.__got: 0x2d0
+  __DATA_CONST.__got: 0x2d8
   __AUTH_CONST.__const: 0x40
-  __AUTH_CONST.__cfstring: 0x4ce0
-  __AUTH_CONST.__objc_const: 0x37f8
+  __AUTH_CONST.__cfstring: 0x4d60
+  __AUTH_CONST.__objc_const: 0x38c0
   __AUTH_CONST.__objc_intobj: 0x198
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0xce0
   __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0x234
+  __DATA.__objc_ivar: 0x24c
   __DATA.__data: 0x420
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 497
-  Symbols:   1208
-  CStrings:  649
+  Functions: 510
+  Symbols:   1229
+  CStrings:  653
 
Symbols:
+ -[WLTransferringViewController _currentUptime]
+ -[WLTransferringViewController _hasItemCount]
+ -[WLTransferringViewController _noteProgressReport]
+ -[WLTransferringViewController _progressReportAge]
+ -[WLTransferringViewController _progressReportsHaveStalled]
+ -[WLTransferringViewController _transferProgressText]
+ -[WLTransferringViewController _updateProgressTextForItemCount]
+ -[WLTransferringViewController displayedProgressText]
+ -[WLTransferringViewController setCompletedItemCount:totalItemCount:]
+ -[WLWelcomeController daemon:didUpdateCompletedItemCount:totalItemCount:]
+ -[WLWelcomeController setMigrationState:]
+ -[WLWelcomeController updateCompletedItemCount:totalItemCount:]
+ _OBJC_CLASS_$_NSProcessInfo
+ _OBJC_IVAR_$_WLTransferringViewController._completedItemCount
+ _OBJC_IVAR_$_WLTransferringViewController._displayedProgressText
+ _OBJC_IVAR_$_WLTransferringViewController._firstItemCountUptime
+ _OBJC_IVAR_$_WLTransferringViewController._lastProgressReportUptime
+ _OBJC_IVAR_$_WLTransferringViewController._reportedStall
+ _OBJC_IVAR_$_WLTransferringViewController._totalItemCount
+ ___73-[WLWelcomeController daemon:didUpdateCompletedItemCount:totalItemCount:]_block_invoke
+ ___block_descriptor_56_e8_32w_e5_v8?0lw32l8
CStrings:
+ "%@ has had no progress report for %.0f seconds. Showing the waiting text in place of the estimate."
+ "%@ received a progress report after a stall."
+ "%@ will update item count. completed_item_count=%lld, total_item_count=%lld"
+ "PROGRESS_TRANSFERRING_NO_RECENT_UPDATE"
```
