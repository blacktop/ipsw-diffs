## StatusKit

> `/System/Library/PrivateFrameworks/StatusKit.framework/StatusKit`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_acfuncs`
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
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__data`

```diff

-149.100.1.0.0
-  __TEXT.__text: 0x45974
+151.100.1.0.0
+  __TEXT.__text: 0x456a0
   __TEXT.__objc_methlist: 0x2128
   __TEXT.__const: 0x1918
-  __TEXT.__gcc_except_tab: 0x8b8
-  __TEXT.__oslogstring: 0x5419
-  __TEXT.__cstring: 0x1d6e
+  __TEXT.__gcc_except_tab: 0x884
+  __TEXT.__oslogstring: 0x5469
+  __TEXT.__cstring: 0x1c7e
   __TEXT.__swift5_typeref: 0x7f0
   __TEXT.__swift5_capture: 0x234
   __TEXT.__constg_swiftt: 0x51c

   __DATA_CONST.__objc_arraydata: 0xd0
   __DATA_CONST.__got: 0x390
   __AUTH_CONST.__const: 0xe68
-  __AUTH_CONST.__cfstring: 0x1200
-  __AUTH_CONST.__objc_const: 0x3890
+  __AUTH_CONST.__cfstring: 0x1180
+  __AUTH_CONST.__objc_const: 0x3850
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__auth_got: 0xaf0
-  __AUTH.__objc_data: 0x460
+  __AUTH.__objc_data: 0x48
   __AUTH.__data: 0x88
   __DATA.__objc_ivar: 0x1d4
-  __DATA.__data: 0x948
-  __DATA.__bss: 0x1810
+  __DATA.__data: 0x860
+  __DATA.__bss: 0x1100
   __DATA.__common: 0x10
-  __DATA_DIRTY.__objc_data: 0x8e8
-  __DATA_DIRTY.__data: 0x7a0
-  __DATA_DIRTY.__bss: 0x170
+  __DATA_DIRTY.__objc_data: 0xd00
+  __DATA_DIRTY.__data: 0x8a0
+  __DATA_DIRTY.__bss: 0x880
   __DATA_DIRTY.__common: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 1705
-  Symbols:   3801
-  CStrings:  541
+  Functions: 1704
+  Symbols:   3798
+  CStrings:  538
 
Symbols:
+ +[NSString(StatusKit) sk_descriptionFromSKUpdatePriority:]
+ -[NSString(StatusKit) sk_clientIdentifierPrefixFromPresenceIdentifier]
+ -[NSString(StatusKit) sk_sha256Hash]
+ -[SKPresence _releaseDaemonConnectionAlreadyLocked]
+ GCC_except_table100
+ GCC_except_table106
+ GCC_except_table110
+ GCC_except_table131
+ GCC_except_table144
+ GCC_except_table149
+ GCC_except_table150
+ GCC_except_table155
+ GCC_except_table158
+ GCC_except_table46
+ GCC_except_table51
+ GCC_except_table75
+ GCC_except_table81
+ GCC_except_table87
+ GCC_except_table92
+ GCC_except_table97
+ __OBJC_$_CATEGORY_CLASS_METHODS_NSString_$_StatusKit
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSString_$_StatusKit
+ __OBJC_$_CATEGORY_NSString_$_StatusKit
+ __OBJC_$_PROP_LIST_NSString_$_StatusKit
+ _objc_msgSend$_releaseDaemonConnectionAlreadyLocked
+ _objc_msgSend$sk_descriptionFromSKUpdatePriority:
+ _objc_msgSend$sk_sha256Hash
- +[NSString(StatusKitAgent) descriptionFromSKUpdatePriority:]
- -[NSString(StatusKitAgent) clientIdentifierPrefixFromPresenceIdentifier]
- -[NSString(StatusKitAgent) ska_appearsToBeEmail]
- -[NSString(StatusKitAgent) ska_sha256Hash]
- GCC_except_table102
- GCC_except_table108
- GCC_except_table112
- GCC_except_table133
- GCC_except_table146
- GCC_except_table151
- GCC_except_table152
- GCC_except_table157
- GCC_except_table160
- GCC_except_table31
- GCC_except_table42
- GCC_except_table48
- GCC_except_table53
- GCC_except_table58
- GCC_except_table63
- GCC_except_table77
- GCC_except_table83
- GCC_except_table89
- GCC_except_table94
- GCC_except_table99
- __OBJC_$_CATEGORY_CLASS_METHODS_NSString_$_StatusKitAgent
- __OBJC_$_CATEGORY_INSTANCE_METHODS_NSString_$_StatusKitAgent
- __OBJC_$_CATEGORY_NSString_$_StatusKitAgent
- __OBJC_$_PROP_LIST_NSString_$_StatusKitAgent
- _objc_msgSend$descriptionFromSKUpdatePriority:
- _objc_msgSend$ska_sha256Hash
CStrings:
+ "Stale daemon disconnection handler, ignoring and not invalidating newer connection."
- "@"
- "Attempted to assert on channel that is not equivalent to active channel"
- "Attempted to retain subscription on channel that is not equivalent to active channel"
- "Attempted to set persistent payload on channel that is not equivalent to active channel"
```
