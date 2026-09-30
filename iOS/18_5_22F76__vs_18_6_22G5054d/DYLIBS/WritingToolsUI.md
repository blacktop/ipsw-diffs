## WritingToolsUI

> `/System/Library/PrivateFrameworks/WritingToolsUI.framework/WritingToolsUI`

```diff

-44.505.100.0.0
-  __TEXT.__text: 0x2ddc0
-  __TEXT.__auth_stubs: 0xd60
-  __TEXT.__objc_methlist: 0x36fc
+44.604.0.0.0
+  __TEXT.__text: 0x2d974
+  __TEXT.__auth_stubs: 0xca0
+  __TEXT.__objc_methlist: 0x37dc
   __TEXT.__const: 0xaa4
   __TEXT.__cstring: 0x1f0e
   __TEXT.__gcc_except_tab: 0x908
-  __TEXT.__oslogstring: 0xc90
+  __TEXT.__oslogstring: 0xc40
   __TEXT.__dlopen_cstrs: 0xb4
   __TEXT.__constg_swiftt: 0x520
-  __TEXT.__swift5_typeref: 0x2ec
+  __TEXT.__swift5_typeref: 0x2de
   __TEXT.__swift5_builtin: 0x64
   __TEXT.__swift5_reflstr: 0x475
   __TEXT.__swift5_fieldmd: 0x3dc

   __TEXT.__swift5_types: 0x34
   __TEXT.__swift5_capture: 0x70
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0xdb8
+  __TEXT.__unwind_info: 0xda8
   __TEXT.__eh_frame: 0xf8
-  __TEXT.__objc_classname: 0x61a
-  __TEXT.__objc_methname: 0x9338
-  __TEXT.__objc_methtype: 0x20a7
-  __TEXT.__objc_stubs: 0x6480
-  __DATA_CONST.__got: 0x4e8
+  __TEXT.__objc_classname: 0x636
+  __TEXT.__objc_methname: 0x94ce
+  __TEXT.__objc_methtype: 0x20b2
+  __TEXT.__objc_stubs: 0x65c0
+  __DATA_CONST.__got: 0x4d0
   __DATA_CONST.__const: 0x900
   __DATA_CONST.__objc_classlist: 0x130
   __DATA_CONST.__objc_catlist: 0x28
-  __DATA_CONST.__objc_protolist: 0xd8
+  __DATA_CONST.__objc_protolist: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x24c8
+  __DATA_CONST.__objc_selrefs: 0x2540
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0xa8
-  __AUTH_CONST.__auth_got: 0x6c0
+  __AUTH_CONST.__auth_got: 0x660
   __AUTH_CONST.__const: 0x768
   __AUTH_CONST.__cfstring: 0x9e0
-  __AUTH_CONST.__objc_const: 0x4e40
-  __AUTH_CONST.__objc_intobj: 0x3d8
+  __AUTH_CONST.__objc_const: 0x4ef0
+  __AUTH_CONST.__objc_intobj: 0x408
   __AUTH.__objc_data: 0xf38
   __AUTH.__data: 0x1e0
-  __DATA.__objc_ivar: 0x274
-  __DATA.__data: 0xbf0
+  __DATA.__objc_ivar: 0x27c
+  __DATA.__data: 0xc50
   __DATA.__bss: 0x9c0
   __DATA.__common: 0x70
   __DATA_DIRTY.__objc_data: 0xa0
-  __DATA_DIRTY.__data: 0x38
+  __DATA_DIRTY.__data: 0x28
   __DATA_DIRTY.__bss: 0x90
   __DATA_DIRTY.__common: 0x20
   - /System/Library/Frameworks/BrowserEngineKit.framework/BrowserEngineKit

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: ECB5D1D3-8660-3FE1-B251-9785DBB84927
+  UUID: FF10195C-B893-326B-8B1C-D15FBA87FC24
   Functions: 1367
-  Symbols:   3853
-  CStrings:  2253
+  Symbols:   3878
+  CStrings:  2272
 
Symbols:
+ +[WTUIActionHostToClient actionForSetRemainingRedoCount:]
+ +[WTUIActionHostToClient actionForSetRemainingUndoCount:]
+ -[WTMainPopoverViewController setRemainingRedoCount:]
+ -[WTMainPopoverViewController setRemainingUndoCount:]
+ -[WTSceneHostedInputDashboardViewController setRemainingRedoCount:]
+ -[WTSceneHostedInputDashboardViewController setRemainingUndoCount:]
+ -[WTWritingToolsController _sendUpdatedUndoRedoCounts]
+ -[WTWritingToolsController remainingRedoCount]
+ -[WTWritingToolsController remainingUndoCount]
+ -[WTWritingToolsController setRemainingRedoCount:]
+ -[WTWritingToolsController setRemainingUndoCount:]
+ GCC_except_table104
+ GCC_except_table126
+ _OBJC_IVAR_$_WTWritingToolsController._remainingRedoCount
+ _OBJC_IVAR_$_WTWritingToolsController._remainingUndoCount
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_WTTextViewDelegate_Internal
+ __OBJC_$_PROTOCOL_METHOD_TYPES_WTTextViewDelegate_Internal
+ __OBJC_$_PROTOCOL_REFS_WTTextViewDelegate_Internal
+ __OBJC_LABEL_PROTOCOL_$_WTTextViewDelegate_Internal
+ __OBJC_PROTOCOL_$_WTTextViewDelegate_Internal
+ _objc_msgSend$_sendUpdatedUndoRedoCounts
+ _objc_msgSend$actionForSetRemainingRedoCount:
+ _objc_msgSend$actionForSetRemainingUndoCount:
+ _objc_msgSend$canRedo
+ _objc_msgSend$canUndo
+ _objc_msgSend$remainingRedoCount
+ _objc_msgSend$remainingUndoCount
+ _objc_msgSend$setRemainingRedoCount:
+ _objc_msgSend$setRemainingUndoCount:
+ _objc_msgSend$unsignedIntValue
- GCC_except_table101
- GCC_except_table123
- GCC_except_table43
- ___62-[WTMainPopoverViewController setFeedbackHiddenDetentEnabled:]_block_invoke
- ___swift_destroy_boxed_opaque_existential_0
- __swiftEmptyArrayStorage
- __swift_stdlib_malloc_size
- _malloc_size
- _memcpy
- _memmove
- _swift_getObjectType
- _swift_isUniquelyReferenced_nonNull_native
- _swift_unknownObjectRetain
- _symbolic _____y_____G s23_ContiguousArrayStorageC s5UInt8V
CStrings:
+ "@24@0:8Q16"
+ "TQ,N,V_remainingRedoCount"
+ "TQ,N,V_remainingUndoCount"
+ "WTTextViewDelegate_Internal"
+ "_remainingRedoCount"
+ "_remainingUndoCount"
+ "_sendUpdatedUndoRedoCounts"
+ "actionForSetRemainingRedoCount:"
+ "actionForSetRemainingUndoCount:"
+ "canRedo"
+ "canUndo"
+ "hostDidAddRemoteView"
+ "inputWarningDidDismiss"
+ "notifyHostIsReady"
+ "popoverDidCloseTransiently"
+ "popoverDidDetach"
+ "remainingRedoCount"
+ "remainingUndoCount"
+ "setRemainingRedoCount:"
+ "setRemainingUndoCount:"
+ "unsignedIntValue"
- "isAvailable: @unknown default"
- "isAvailable: unavailable, info = %s"

```
