## MDM

> `/System/Library/PrivateFrameworks/MDM.framework/MDM`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__cstring`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-111.0.0.0.0
-  __TEXT.__text: 0x58544
+113.0.2.0.0
+  __TEXT.__text: 0x585d0
   __TEXT.__objc_methlist: 0x43a4
   __TEXT.__const: 0x1c2
   __TEXT.__gcc_except_tab: 0xf08
Symbols:
+ +[MDMMCInterface clearPasscodeWithEscrowKeybagData:secretContext:outError:]
+ _objc_msgSend$clearPasscodeWithEscrowKeybagData:secretContext:outError:
- +[MDMMCInterface clearPasscodeWithEscrowKeybagData:secret:outError:]
- _objc_msgSend$clearPasscodeWithEscrowKeybagData:secret:outError:
Functions:
~ -[MDMParser _clearPasscode:] : 548 -> 688
```
