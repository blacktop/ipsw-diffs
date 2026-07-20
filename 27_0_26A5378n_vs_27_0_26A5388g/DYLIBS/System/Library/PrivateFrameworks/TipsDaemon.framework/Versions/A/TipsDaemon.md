## TipsDaemon

> `/System/Library/PrivateFrameworks/TipsDaemon.framework/Versions/A/TipsDaemon`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`

```diff

-855.0.0.0.0
-  __TEXT.__text: 0x89fb8
+857.0.0.0.0
+  __TEXT.__text: 0x8a030
   __TEXT.__objc_methlist: 0x36b8
   __TEXT.__const: 0x2be8
   __TEXT.__oslogstring: 0x1e59

   __DATA_CONST.__objc_classlist: 0x510
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2398
+  __DATA_CONST.__objc_selrefs: 0x23b0
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x1b0
   __DATA_CONST.__objc_arraydata: 0x58

   __AUTH_CONST.__objc_intobj: 0x168
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__auth_got: 0xd98
-  __AUTH.__objc_data: 0x10c0
-  __AUTH.__data: 0x118
+  __AUTH.__objc_data: 0xeb0
+  __AUTH.__data: 0x50
   __DATA.__objc_ivar: 0x210
-  __DATA.__data: 0x860
-  __DATA.__bss: 0x1c80
+  __DATA.__data: 0x838
+  __DATA.__bss: 0x1c00
   __DATA.__common: 0x8
-  __DATA_DIRTY.__objc_data: 0x3120
-  __DATA_DIRTY.__data: 0xea0
-  __DATA_DIRTY.__bss: 0x1660
+  __DATA_DIRTY.__objc_data: 0x3330
+  __DATA_DIRTY.__data: 0xf98
+  __DATA_DIRTY.__bss: 0x16e0
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/Contacts.framework/Versions/A/Contacts
   - /System/Library/Frameworks/CoreBluetooth.framework/Versions/A/CoreBluetooth

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 3006
-  Symbols:   4291
+  Symbols:   4294
   CStrings:  689
 
Symbols:
+ _objc_msgSend$isMacUI
+ _objc_msgSend$isPadUI
+ _objc_msgSend$siriCollectionIdentifier
Functions:
~ -[TPSTipsManager welcomeCollectionFromContentPackage:] : 256 -> 376
```
