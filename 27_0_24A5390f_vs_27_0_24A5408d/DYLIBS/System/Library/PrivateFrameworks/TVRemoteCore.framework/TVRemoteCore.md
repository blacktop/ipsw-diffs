## TVRemoteCore

> `/System/Library/PrivateFrameworks/TVRemoteCore.framework/TVRemoteCore`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__lazy_load_got`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-627.0.19.0.0
-  __TEXT.__text: 0x487b4
+627.0.28.0.0
+  __TEXT.__text: 0x48670
   __TEXT.__lazy_helpers: 0x580
-  __TEXT.__objc_methlist: 0x64e0
-  __TEXT.__const: 0x2a0
-  __TEXT.__oslogstring: 0x6b4c
-  __TEXT.__cstring: 0x3784
-  __TEXT.__gcc_except_tab: 0xafc
-  __TEXT.__unwind_info: 0x1218
+  __TEXT.__objc_methlist: 0x64d0
+  __TEXT.__const: 0x240
+  __TEXT.__oslogstring: 0x6b90
+  __TEXT.__cstring: 0x372c
+  __TEXT.__gcc_except_tab: 0xb14
+  __TEXT.__unwind_info: 0x1210
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3098
+  __DATA_CONST.__objc_selrefs: 0x3090
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x210
-  __DATA_CONST.__objc_arraydata: 0x120
+  __DATA_CONST.__objc_arraydata: 0x110
   __DATA_CONST.__got: 0x470
   __AUTH_CONST.__const: 0x480
-  __AUTH_CONST.__cfstring: 0x4aa0
+  __AUTH_CONST.__cfstring: 0x4a60
   __AUTH_CONST.__objc_const: 0x9f88
   __AUTH_CONST.__lazy_load_got: 0x80
   __AUTH_CONST.__objc_intobj: 0x288

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2138
-  Symbols:   4768
-  CStrings:  1301
+  Functions: 2139
+  Symbols:   4765
+  CStrings:  1299
 
Symbols:
+ -[TVRCRPCompanionLinkClientWrapper _toggleCaptions:completion:]
+ GCC_except_table103
+ GCC_except_table113
+ GCC_except_table118
+ GCC_except_table123
+ GCC_except_table129
+ GCC_except_table133
+ GCC_except_table140
+ GCC_except_table145
+ GCC_except_table35
+ GCC_except_table40
+ GCC_except_table87
+ GCC_except_table90
+ GCC_except_table97
+ ___63-[TVRCRPCompanionLinkClientWrapper _toggleCaptions:completion:]_block_invoke
+ _objc_msgSend$_toggleCaptions:completion:
- -[TVRCMediaEventsManager supportedCaptionEvents]
- -[TVRCRPCompanionLinkClientWrapper toggleCaptions:]
- -[TVRCRapportMediaEventsManager supportedCaptionEvents]
- GCC_except_table101
- GCC_except_table111
- GCC_except_table116
- GCC_except_table121
- GCC_except_table127
- GCC_except_table131
- GCC_except_table138
- GCC_except_table143
- GCC_except_table34
- GCC_except_table39
- GCC_except_table77
- GCC_except_table88
- GCC_except_table91
- _objc_msgSend$currentSetting
- _objc_msgSend$supportedCaptionEvents
- _objc_msgSend$toggleCaptions:
CStrings:
+ "Caption toggle send failed. error=%{public}@"
+ "Ignoring caption toggle event; current caption state is unknown. %@"
+ "toggleCaptions to: %{public,bool}d; %@"
- "%s: %{public,bool}d %@"
- "-[TVRCRPCompanionLinkClientWrapper toggleCaptions:]"
- "CaptionsAlwaysOn"
- "CaptionsForcedOnly"
- "Supported Caption Events for current settings=%s, events=\n%@"
```
