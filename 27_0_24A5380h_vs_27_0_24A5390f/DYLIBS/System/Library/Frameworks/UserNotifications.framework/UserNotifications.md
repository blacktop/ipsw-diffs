## UserNotifications

> `/System/Library/Frameworks/UserNotifications.framework/UserNotifications`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__cstring`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-713.0.0.0.0
+717.0.0.0.0
   __TEXT.__text: 0x2f710
   __TEXT.__objc_methlist: 0x37d8
   __TEXT.__cstring: 0x3661
Functions:
~ +[NSError(UserNotifications) _un_descriptionForUNErrorCode:] : 228 -> 212
~ +[NSError(UserNotifications) _un_descriptionForUNPrivateErrorCode:] : 164 -> 180
```
