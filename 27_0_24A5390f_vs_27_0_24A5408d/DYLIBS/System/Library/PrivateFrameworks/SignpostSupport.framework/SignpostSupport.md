## SignpostSupport

> `/System/Library/PrivateFrameworks/SignpostSupport.framework/SignpostSupport`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__weak_got`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_intobj`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-202.0.0.0.0
-  __TEXT.__text: 0x7753c
-  __TEXT.__objc_methlist: 0xa014
+203.0.0.0.0
+  __TEXT.__text: 0x7757c
+  __TEXT.__objc_methlist: 0xa02c
   __TEXT.__const: 0x19f8
   __TEXT.__cstring: 0x1a737
   __TEXT.__oslogstring: 0xef4

   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3b68
+  __DATA_CONST.__objc_selrefs: 0x3b78
   __DATA_CONST.__objc_superrefs: 0x488
   __DATA_CONST.__objc_arraydata: 0x50c8
   __DATA_CONST.__got: 0x470
   __AUTH_CONST.__const: 0x1868
   __AUTH_CONST.__cfstring: 0x1ca60
-  __AUTH_CONST.__objc_const: 0x16c08
+  __AUTH_CONST.__objc_const: 0x16c38
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x408
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_intobj: 0x1e0
   __AUTH_CONST.__auth_got: 0x0
-  __DATA.__objc_ivar: 0xf2c
+  __DATA.__objc_ivar: 0xf30
   __DATA.__data: 0x1180
   __DATA.__bss: 0x410
   __DATA_DIRTY.__objc_data: 0x3390

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 4103
-  Symbols:   8818
+  Functions: 4105
+  Symbols:   8824
   CStrings:  3920
 
Symbols:
+ -[SignpostSupportObjectExtractor didComplete]
+ -[SignpostSupportObjectExtractor setDidComplete:]
+ GCC_except_table102
+ GCC_except_table104
+ GCC_except_table105
+ GCC_except_table108
+ GCC_except_table118
+ GCC_except_table119
+ GCC_except_table127
+ GCC_except_table128
+ GCC_except_table144
+ GCC_except_table147
+ GCC_except_table151
+ GCC_except_table155
+ GCC_except_table156
+ GCC_except_table16
+ GCC_except_table163
+ GCC_except_table165
+ GCC_except_table173
+ GCC_except_table174
+ GCC_except_table180
+ GCC_except_table191
+ GCC_except_table192
+ GCC_except_table199
+ GCC_except_table201
+ GCC_except_table212
+ GCC_except_table218
+ GCC_except_table220
+ GCC_except_table227
+ GCC_except_table228
+ GCC_except_table238
+ GCC_except_table241
+ GCC_except_table246
+ GCC_except_table249
+ GCC_except_table251
+ GCC_except_table253
+ GCC_except_table256
+ GCC_except_table267
+ GCC_except_table29
+ GCC_except_table303
+ GCC_except_table34
+ GCC_except_table36
+ GCC_except_table37
+ GCC_except_table47
+ GCC_except_table48
+ GCC_except_table53
+ GCC_except_table54
+ GCC_except_table56
+ GCC_except_table57
+ GCC_except_table60
+ GCC_except_table61
+ GCC_except_table65
+ GCC_except_table66
+ GCC_except_table68
+ GCC_except_table69
+ GCC_except_table78
+ GCC_except_table8
+ GCC_except_table80
+ GCC_except_table84
+ GCC_except_table87
+ GCC_except_table88
+ GCC_except_table97
+ _OBJC_IVAR_$_SignpostSupportObjectExtractor._didComplete
+ _objc_msgSend$didComplete
+ _objc_msgSend$setDidComplete:
+ _objc_msgSend$set_stopProcessingBlock:
- GCC_except_table110
- GCC_except_table111
- GCC_except_table12
- GCC_except_table121
- GCC_except_table133
- GCC_except_table138
- GCC_except_table140
- GCC_except_table141
- GCC_except_table143
- GCC_except_table150
- GCC_except_table157
- GCC_except_table160
- GCC_except_table167
- GCC_except_table168
- GCC_except_table170
- GCC_except_table171
- GCC_except_table177
- GCC_except_table178
- GCC_except_table179
- GCC_except_table188
- GCC_except_table195
- GCC_except_table198
- GCC_except_table205
- GCC_except_table206
- GCC_except_table21
- GCC_except_table215
- GCC_except_table216
- GCC_except_table221
- GCC_except_table225
- GCC_except_table226
- GCC_except_table233
- GCC_except_table236
- GCC_except_table240
- GCC_except_table244
- GCC_except_table247
- GCC_except_table250
- GCC_except_table252
- GCC_except_table254
- GCC_except_table257
- GCC_except_table265
- GCC_except_table273
- GCC_except_table302
- GCC_except_table41
- GCC_except_table42
- GCC_except_table45
- GCC_except_table46
- GCC_except_table51
- GCC_except_table59
- GCC_except_table63
- GCC_except_table72
- GCC_except_table75
- GCC_except_table79
- GCC_except_table81
- GCC_except_table83
- GCC_except_table86
- GCC_except_table9
- GCC_except_table93
- GCC_except_table95
- GCC_except_table96
- _objc_msgSend$setNotificationProcessingQueue:
```
