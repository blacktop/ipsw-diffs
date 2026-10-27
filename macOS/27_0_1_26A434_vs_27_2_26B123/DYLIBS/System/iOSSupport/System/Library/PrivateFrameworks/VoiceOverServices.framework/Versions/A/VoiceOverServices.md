## VoiceOverServices

> `/System/iOSSupport/System/Library/PrivateFrameworks/VoiceOverServices.framework/Versions/A/VoiceOverServices`

```diff

-3240.0.1.2.0
-  __TEXT.__text: 0x288dc
-  __TEXT.__objc_methlist: 0x292c
+3245.8.6.2.0
+  __TEXT.__text: 0x299a4
+  __TEXT.__objc_methlist: 0x2994
   __TEXT.__dlopen_cstrs: 0x41
-  __TEXT.__const: 0x40
+  __TEXT.__const: 0x50
   __TEXT.__gcc_except_tab: 0xc4
-  __TEXT.__cstring: 0x637a
-  __TEXT.__oslogstring: 0x39e
-  __TEXT.__unwind_info: 0x560
+  __TEXT.__cstring: 0x63d0
+  __TEXT.__oslogstring: 0x452
+  __TEXT.__unwind_info: 0x568
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0xc0
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x18c0
+  __DATA_CONST.__objc_selrefs: 0x1900
   __DATA_CONST.__objc_superrefs: 0x90
   __DATA_CONST.__objc_arraydata: 0x20
   __DATA_CONST.__got: 0x180
-  __AUTH_CONST.__const: 0x31c0
-  __AUTH_CONST.__cfstring: 0x76a0
-  __AUTH_CONST.__objc_const: 0x3b88
+  __AUTH_CONST.__const: 0x3220
+  __AUTH_CONST.__cfstring: 0x7720
+  __AUTH_CONST.__objc_const: 0x3be8
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__auth_got: 0x0
-  __DATA.__objc_ivar: 0xfc
-  __DATA.__data: 0xde8
-  __DATA.__bss: 0x618
+  __DATA.__objc_ivar: 0x100
+  __DATA.__data: 0xdf0
+  __DATA.__bss: 0x5d8
   __DATA_DIRTY.__objc_data: 0x780
-  __DATA_DIRTY.__bss: 0x12a0
+  __DATA_DIRTY.__bss: 0x1310
   - /System/Library/Frameworks/CoreBluetooth.framework/Versions/A/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1251
-  Symbols:   3544
-  CStrings:  991
+  Functions: 1262
+  Symbols:   3572
+  CStrings:  999
 
Symbols:
+ +[VOSCommand BraillePanPageDown]
+ +[VOSCommand BraillePanPageUp]
+ +[VOSCommand ReadCurrentItem]
+ -[VOSCommandProfile _coalesceDuplicateProfileCommands]
+ -[VOSCommandProfile _isUnboundProfileCommand:]
+ -[VOSCommandProfile _releaseGesturesShadowedByUnboundCommands]
+ -[VOSCommandProfile requiresResave]
+ -[_VOSProfileMode removeCommand:]
+ BraillePanPageDown._Command
+ BraillePanPageDown.onceToken
+ BraillePanPageUp._Command
+ BraillePanPageUp.onceToken
+ GCC_except_table1143
+ OBJC_IVAR_$_VOSCommandProfile._requiresResave
+ ReadCurrentItem._Command
+ ReadCurrentItem.onceToken
+ ___29+[VOSCommand ReadCurrentItem]_block_invoke
+ ___30+[VOSCommand BraillePanPageUp]_block_invoke
+ ___32+[VOSCommand BraillePanPageDown]_block_invoke
+ _kVOTEventCommandBraillePanPageDown
+ _kVOTEventCommandBraillePanPageUp
+ _kVOTEventCommandOutputCurrentElement
+ _objc_msgSend$BraillePanPageDown
+ _objc_msgSend$BraillePanPageUp
+ _objc_msgSend$ReadCurrentItem
+ _objc_msgSend$_coalesceDuplicateProfileCommands
+ _objc_msgSend$_isUnboundProfileCommand:
+ _objc_msgSend$_releaseGesturesShadowedByUnboundCommands
+ _objc_msgSend$removeCommand:
+ _objc_msgSend$requiresResave
+ _objc_msgSend$secondaryCommands
- GCC_except_table1136
- _kVOTEventCommandBraillePlanarPanLeft
- _kVOTEventCommandBraillePlanarPanRight
CStrings:
+ "!"
+ "BraillePanPageDown"
+ "BraillePanPageUp"
+ "Coalesced %lu duplicate profile command(s) in mode %@"
+ "Gesture %@ is claimed by more than one command in mode %@. Leaving it alone"
+ "ReadCurrentItem"
+ "Released %lu gesture(s) shadowed by %@ in mode %@"
+ "VOTEventCommandBraillePanPageDown"
+ "VOTEventCommandBraillePanPageUp"
+ "VOTEventCommandOutputCurrentElement"
- "VOTEventCommandBraillePlanarPanLeft"
- "VOTEventCommandBraillePlanarPanRight"
```
