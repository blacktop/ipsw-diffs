## HealthRecordsPlugin

> `/System/Library/PrivateFrameworks/HealthRecordsPlugin.framework/HealthRecordsPlugin`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_proto`
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
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-7027.0.64.0.0
+7027.0.67.2.1
   __TEXT.__text: 0xb6428
   __TEXT.__objc_methlist: 0x780c
   __TEXT.__const: 0xa30
-  __TEXT.__cstring: 0x979f
+  __TEXT.__cstring: 0x978f
   __TEXT.__oslogstring: 0xfdb7
   __TEXT.__gcc_except_tab: 0x1968
   __TEXT.__ustring: 0x7e
CStrings:
+ "SELECT %@, %@, %@ FROM %@ WHERE %@ = ? AND %@ = ? AND %@ = ?"
+ "SELECT %@, %@, %@, %@, %@ FROM %@ WHERE %@ = ? AND %@ = ? AND %@ = ? AND %@ = ? AND (%@ = ? OR %@ > ?)"
+ "SELECT res.%@                     FROM %@ AS res                     LEFT JOIN %@ AS last ON res.%@ = last.%@                     WHERE res.%@ = ? AND (last.%@ < ? OR last.%@ IS NULL)"
+ "SELECT res.%@, res.%@, res.%@, last.%@                     FROM %@ AS res                     LEFT JOIN %@ AS last ON res.%@ = last.%@                     WHERE res.%@ = ?"
- "SELECT %@, %@, %@ FROM %@ WHERE %@ LIKE ? AND %@ LIKE ? AND %@ = ?"
- "SELECT %@, %@, %@, %@, %@ FROM %@ WHERE %@ LIKE ? AND %@ LIKE ? AND %@ = ? AND %@ LIKE ? AND (%@ = ? OR %@ > ?)"
- "SELECT res.%@                     FROM %@ AS res                     LEFT JOIN %@ AS last ON res.%@ = last.%@                     WHERE res.%@ LIKE ? AND (last.%@ < ? OR last.%@ IS NULL)"
- "SELECT res.%@, res.%@, res.%@, last.%@                     FROM %@ AS res                     LEFT JOIN %@ AS last ON res.%@ = last.%@                     WHERE res.%@ LIKE ?"
```
