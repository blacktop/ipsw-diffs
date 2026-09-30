## IMAP

> `/System/Library/PrivateFrameworks/IMAP.framework/Versions/A/IMAP`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-3895.100.17.0.0
-  __TEXT.__text: 0x5673c
-  __TEXT.__objc_methlist: 0x686c
+3897.100.8.1.1
+  __TEXT.__text: 0x56790
+  __TEXT.__objc_methlist: 0x6884
   __TEXT.__cstring: 0x4181
   __TEXT.__const: 0x250
   __TEXT.__gcc_except_tab: 0x1c0c

   __DATA_CONST.__objc_classlist: 0x498
   __DATA_CONST.__objc_protolist: 0x160
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2f40
+  __DATA_CONST.__objc_selrefs: 0x2f50
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x2c0
   __DATA_CONST.__objc_arraydata: 0x8
   __DATA_CONST.__got: 0x798
   __AUTH_CONST.__const: 0x1420
   __AUTH_CONST.__cfstring: 0x4ba0
-  __AUTH_CONST.__objc_const: 0xbe78
+  __AUTH_CONST.__objc_const: 0xbe98
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_got: 0x0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 2091
-  Symbols:   5417
+  Symbols:   5418
   CStrings:  819
 
Symbols:
+ _objc_msgSend$setInitialSyncCompleted:
Functions:
~ -[IMAPTaskManager activityDidFinish:] : 2488 -> 2520
~ -[IMAPTaskManager _syncMailboxWithDataSource:withIMAPMailbox:fromStatus:forceFullSync:syncType:] : 976 -> 1028
```
