## AddressBook

> `/System/Library/Frameworks/AddressBook.framework/Versions/A/AddressBook`

```diff

-2765.100.1.1.1
-  __TEXT.__text: 0x103944
-  __TEXT.__objc_methlist: 0x17e3c
-  __TEXT.__const: 0x340
-  __TEXT.__gcc_except_tab: 0x1718
-  __TEXT.__cstring: 0x9bc0
+2768.200.91.0.0
+  __TEXT.__text: 0x103ec4
+  __TEXT.__objc_methlist: 0x17e9c
+  __TEXT.__const: 0x348
+  __TEXT.__gcc_except_tab: 0x172c
+  __TEXT.__cstring: 0x9bdb
   __TEXT.__ustring: 0x466
   __TEXT.__dlopen_cstrs: 0xdbe
   __TEXT.__oslogstring: 0xae8
-  __TEXT.__unwind_info: 0x54a0
+  __TEXT.__unwind_info: 0x54c0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0xb8
   __DATA_CONST.__objc_protolist: 0x308
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xbec0
+  __DATA_CONST.__objc_selrefs: 0xbf08
   __DATA_CONST.__objc_protorefs: 0x40
   __DATA_CONST.__objc_superrefs: 0x9a0
   __DATA_CONST.__objc_arraydata: 0x150
   __DATA_CONST.__got: 0x1c18
-  __AUTH_CONST.__const: 0x43f0
+  __AUTH_CONST.__const: 0x4420
   __AUTH_CONST.__cfstring: 0x8e80
-  __AUTH_CONST.__objc_const: 0x25438
+  __AUTH_CONST.__objc_const: 0x25468
   __AUTH_CONST.__objc_intobj: 0x210
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_arrayobj: 0x48

   __AUTH_CONST.__auth_ptr: 0x0
   __AUTH.__objc_data: 0x7b20
   __AUTH.__data: 0x120
-  __DATA.__objc_ivar: 0x144c
-  __DATA.__data: 0x2598
+  __DATA.__objc_ivar: 0x1450
+  __DATA.__data: 0x2418
   __DATA.__bss: 0x1278
   __DATA_DIRTY.__objc_data: 0x1b80
-  __DATA_DIRTY.__data: 0x10
+  __DATA_DIRTY.__data: 0x190
   __DATA_DIRTY.__bss: 0x280
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/CoreData.framework/Versions/A/CoreData

   - /usr/lib/libDiagnosticMessagesClient.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 8149
-  Symbols:   19284
-  CStrings:  1657
+  Functions: 8158
+  Symbols:   19304
+  CStrings:  1658
 
Symbols:
+ -[ABMainListOutlineView .cxx_destruct]
+ -[ABMainListOutlineView ab_configureDraggingItems:atPointInSelf:]
+ -[ABMainListOutlineView ab_handledControlClickEvent:]
+ -[ABMainListOutlineView ab_updateControlClickEventMonitor]
+ -[ABMainListOutlineView beginDraggingSessionWithItems:gesture:source:]
+ -[ABMainListOutlineView controlClickEventMonitor]
+ -[ABMainListOutlineView dealloc]
+ -[ABMainListOutlineView setControlClickEventMonitor:]
+ -[ABMainListOutlineView viewDidMoveToWindow]
+ OBJC_IVAR_$_ABMainListOutlineView._controlClickEventMonitor
+ ___58-[ABMainListOutlineView ab_updateControlClickEventMonitor]_block_invoke
+ ___65-[ABMainListOutlineView ab_configureDraggingItems:atPointInSelf:]_block_invoke
+ ___block_descriptor_40_e8_32w_e26_"NSEvent"16?0"NSEvent"8l
+ _objc_msgSend$ab_configureDraggingItems:atPointInSelf:
+ _objc_msgSend$ab_handledControlClickEvent:
+ _objc_msgSend$ab_updateControlClickEventMonitor
+ _objc_msgSend$addLocalMonitorForEventsMatchingMask:handler:
+ _objc_msgSend$controlClickEventMonitor
+ _objc_msgSend$hitTest:
+ _objc_msgSend$locationInView:
+ _objc_msgSend$removeMonitor:
+ _objc_msgSend$setControlClickEventMonitor:
- -[ABMainListOutlineView mouseDown:]
- ___68-[ABMainListOutlineView beginDraggingSessionWithItems:event:source:]_block_invoke
CStrings:
+ "@\"NSEvent\"16@?0@\"NSEvent\"8"
```
