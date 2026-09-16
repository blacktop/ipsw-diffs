## LightSourceSupport

> `/System/Library/PrivateFrameworks/LightSourceSupport.framework/LightSourceSupport`

```diff

-8.0.74.0.0
-  __TEXT.__text: 0xebb8
-  __TEXT.__objc_methlist: 0xbac
+8.1.5.0.0
+  __TEXT.__text: 0xf71c
+  __TEXT.__objc_methlist: 0xbc4
   __TEXT.__const: 0x100
-  __TEXT.__cstring: 0xb7b
-  __TEXT.__oslogstring: 0x863
-  __TEXT.__gcc_except_tab: 0x42c
-  __TEXT.__unwind_info: 0x710
+  __TEXT.__cstring: 0xb98
+  __TEXT.__oslogstring: 0xa29
+  __TEXT.__gcc_except_tab: 0x444
+  __TEXT.__unwind_info: 0x738
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x598
+  __DATA_CONST.__objc_selrefs: 0x5c8
   __DATA_CONST.__objc_superrefs: 0xc0
   __DATA_CONST.__objc_arraydata: 0x20
-  __DATA_CONST.__got: 0x178
+  __DATA_CONST.__got: 0x180
   __AUTH_CONST.__const: 0x300
-  __AUTH_CONST.__cfstring: 0x680
-  __AUTH_CONST.__objc_const: 0x30b0
+  __AUTH_CONST.__cfstring: 0x6a0
+  __AUTH_CONST.__objc_const: 0x3120
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_doubleobj: 0x130
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH_CONST.__auth_got: 0x3e0
+  __AUTH_CONST.__auth_got: 0x3f0
   __AUTH.__thread_vars: 0x30
   __AUTH.__thread_bss: 0x38
-  __DATA.__objc_ivar: 0x274
+  __DATA.__objc_ivar: 0x280
   __DATA.__data: 0x2a8
   __DATA_DIRTY.__objc_data: 0x960
   __DATA_DIRTY.__bss: 0x180

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 461
-  Symbols:   1116
-  CStrings:  228
+  Functions: 473
+  Symbols:   1139
+  CStrings:  242
 
Symbols:
+ -[LSSCAService _enabledIntegratedDisplayIds]
+ -[LSSCAService _integratedDisplayWithId:]
+ -[LSSController _handleDisplayLinkStall]
+ -[LSSDisplayLinkResampler displayLinkStalledHandler]
+ -[LSSDisplayLinkResampler setDisplayLinkStalledHandler:]
+ GCC_except_table17
+ _OBJC_CLASS_$_NSMutableString
+ _OBJC_IVAR_$_LSSDisplayLinkResampler._displayLinkStalledHandler
+ _OBJC_IVAR_$_LSSDisplayLinkResampler._lastFireTime
+ _OBJC_IVAR_$_LSSDisplayLinkResampler._stallReported
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_13
+ ___32-[LSSController _setProviderTo:]_block_invoke
+ ___32-[LSSController _setProviderTo:]_block_invoke_2
+ ___NSArray0__struct
+ _objc_msgSend$appendFormat:
+ _objc_msgSend$length
+ _objc_msgSend$setDisplayLinkStalledHandler:
+ _objc_msgSend$string
+ _objc_msgSend$unsignedIntValue
+ _objc_release_x28
+ _objc_retain
- -[LSSCAService _integratedDisplayUsingGlobalLight]
CStrings:
+ " "
+ "%s%u:%s%s"
+ "+light"
+ "Q"
+ "changing provider: %{public}@"
+ "changing provider: %{public}@. display: %u"
+ "display link display: %u. active display"
+ "display link display: %u. using global light"
+ "display link has not fired in %f s. its display is not refreshing"
+ "display link recovered"
+ "display link stalled on display %u but it is still the display we would pick"
+ "display link stalled. active display moved to %u"
+ "integrated displays: [%{public}@]"
+ "no enabled integrated display. falling back to main display: %u"
+ "off"
+ "on"
- "1"
- "changing provider"
```
