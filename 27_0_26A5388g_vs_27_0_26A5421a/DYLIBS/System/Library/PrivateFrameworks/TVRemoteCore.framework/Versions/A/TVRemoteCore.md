## TVRemoteCore

> `/System/Library/PrivateFrameworks/TVRemoteCore.framework/Versions/A/TVRemoteCore`

```diff

-627.0.19.0.0
-  __TEXT.__text: 0x4bd8c
+627.0.28.0.0
+  __TEXT.__text: 0x4bc2c
   __TEXT.__objc_methlist: 0x63a8
-  __TEXT.__const: 0x290
-  __TEXT.__cstring: 0x367f
-  __TEXT.__gcc_except_tab: 0xb04
-  __TEXT.__oslogstring: 0x6653
+  __TEXT.__const: 0x230
+  __TEXT.__cstring: 0x3627
+  __TEXT.__gcc_except_tab: 0xb1c
+  __TEXT.__oslogstring: 0x6697
   __TEXT.__unwind_info: 0x11f0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_selrefs: 0x2f90
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x208
-  __DATA_CONST.__objc_arraydata: 0x108
+  __DATA_CONST.__objc_arraydata: 0xf8
   __DATA_CONST.__got: 0x4a0
   __AUTH_CONST.__const: 0x1300
-  __AUTH_CONST.__cfstring: 0x49e0
-  __AUTH_CONST.__objc_const: 0x9d88
+  __AUTH_CONST.__cfstring: 0x49a0
+  __AUTH_CONST.__objc_const: 0x9d90
   __AUTH_CONST.__objc_intobj: 0x288
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_doubleobj: 0x60

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2153
-  Symbols:   4742
-  CStrings:  1268
+  Functions: 2154
+  Symbols:   4739
+  CStrings:  1266
 
Symbols:
+ -[TVRCRPCompanionLinkClientWrapper _toggleCaptions:completion:]
+ GCC_except_table100
+ GCC_except_table102
+ GCC_except_table110
+ GCC_except_table112
+ GCC_except_table114
+ GCC_except_table120
+ GCC_except_table130
+ GCC_except_table135
+ GCC_except_table140
+ GCC_except_table146
+ GCC_except_table152
+ GCC_except_table159
+ GCC_except_table166
+ GCC_except_table42
+ GCC_except_table47
+ GCC_except_table51
+ GCC_except_table96
+ GCC_except_table98
+ ___63-[TVRCRPCompanionLinkClientWrapper _toggleCaptions:completion:]_block_invoke
+ _objc_msgSend$_toggleCaptions:completion:
- -[TVRCMediaEventsManager supportedCaptionEvents]
- -[TVRCRPCompanionLinkClientWrapper toggleCaptions:]
- -[TVRCRapportMediaEventsManager supportedCaptionEvents]
- GCC_except_table101
- GCC_except_table109
- GCC_except_table111
- GCC_except_table117
- GCC_except_table127
- GCC_except_table132
- GCC_except_table137
- GCC_except_table143
- GCC_except_table149
- GCC_except_table156
- GCC_except_table163
- GCC_except_table41
- GCC_except_table46
- GCC_except_table49
- GCC_except_table93
- GCC_except_table95
- GCC_except_table97
- GCC_except_table99
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
