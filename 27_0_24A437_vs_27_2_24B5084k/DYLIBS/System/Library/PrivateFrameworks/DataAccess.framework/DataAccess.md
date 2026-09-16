## DataAccess

> `/System/Library/PrivateFrameworks/DataAccess.framework/DataAccess`

```diff

-2708.0.0.0.0
-  __TEXT.__text: 0x3999c
-  __TEXT.__objc_methlist: 0x482c
+2708.1.5.0.0
+  __TEXT.__text: 0x39c78
+  __TEXT.__objc_methlist: 0x488c
   __TEXT.__const: 0x190
   __TEXT.__gcc_except_tab: 0x1694
   __TEXT.__cstring: 0x32dc
-  __TEXT.__oslogstring: 0x537f
+  __TEXT.__oslogstring: 0x53d9
   __TEXT.__dlopen_cstrs: 0x102
-  __TEXT.__unwind_info: 0x14a8
+  __TEXT.__unwind_info: 0x14b8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2da0
+  __DATA_CONST.__objc_selrefs: 0x2dc0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x178
   __DATA_CONST.__objc_arraydata: 0x8
   __DATA_CONST.__got: 0x750
   __AUTH_CONST.__const: 0x400
   __AUTH_CONST.__cfstring: 0x31a0
-  __AUTH_CONST.__objc_const: 0x7220
+  __AUTH_CONST.__objc_const: 0x72a8
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_got: 0x0
-  __DATA.__objc_ivar: 0x358
+  __DATA.__objc_ivar: 0x360
   __DATA.__data: 0x420
   __DATA_DIRTY.__objc_data: 0x1400
   __DATA_DIRTY.__bss: 0x114

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1607
-  Symbols:   3871
-  CStrings:  778
+  Functions: 1616
+  Symbols:   3885
+  CStrings:  779
 
Symbols:
+ -[DAABLegacyContainer hasUserVisibleChanges]
+ -[DAABLegacyContainer setUserVisibleChanges:]
+ -[DAABLegacyContainer userVisibleChanges]
+ -[DAContactsContainer hasUserVisibleChanges]
+ -[DAContactsContainer setUserVisibleChanges:]
+ -[DAContactsContainer userVisibleChanges]
+ -[DALocalDBHelper abSaveDBSuppressingChangeNotifications]
+ _ABAddressBookSetSuppressChangeNotifications
+ _OBJC_IVAR_$_DAABLegacyContainer._userVisibleChanges
+ _OBJC_IVAR_$_DAContactsContainer._userVisibleChanges
+ ___57-[DALocalDBHelper abSaveDBSuppressingChangeNotifications]_block_invoke
+ _objc_msgSend$markedAsDefault
+ _objc_msgSend$setUserVisibleChanges:
+ _objc_msgSend$userVisibleChanges
CStrings:
+ "abSaveDBSuppressingChangeNotifications is unsupported under modern Contacts framework :%@"
```
