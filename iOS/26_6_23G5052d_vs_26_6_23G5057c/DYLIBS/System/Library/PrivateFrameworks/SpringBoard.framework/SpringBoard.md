## SpringBoard

> `/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`

```diff

-  __TEXT.__text: 0xb1c2ec
+  __TEXT.__text: 0xb1c388
   __TEXT.__auth_stubs: 0x55a0
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0xb9a38
-  __TEXT.__const: 0x130f0
-  __TEXT.__oslogstring: 0x5ef0b
-  __TEXT.__cstring: 0x7e6f4
+  __TEXT.__objc_methlist: 0xb9a58
+  __TEXT.__const: 0x13100
+  __TEXT.__oslogstring: 0x5ef30
+  __TEXT.__cstring: 0x7e712
   __TEXT.__gcc_except_tab: 0x195ac
   __TEXT.__ustring: 0xcce
   __TEXT.__dlopen_cstrs: 0x313
   __TEXT.__unwind_info: 0x303f0
   __TEXT.__eh_frame: 0x80
-  __TEXT.__objc_classname: 0x22553
-  __TEXT.__objc_methname: 0x1d5f11
-  __TEXT.__objc_methtype: 0x4d89f
+  __TEXT.__objc_classname: 0x22570
+  __TEXT.__objc_methname: 0x1d5f02
+  __TEXT.__objc_methtype: 0x4d8bf
   __TEXT.__objc_stubs: 0xf6a00
-  __DATA_CONST.__got: 0xa4b8
+  __DATA_CONST.__got: 0xa4c0
   __DATA_CONST.__const: 0x1cf88
-  __DATA_CONST.__objc_classlist: 0x5318
+  __DATA_CONST.__objc_classlist: 0x5320
   __DATA_CONST.__objc_catlist: 0x358
   __DATA_CONST.__objc_nlcatlist: 0x8
   __DATA_CONST.__objc_protolist: 0x2930
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x4b820
   __DATA_CONST.__objc_protorefs: 0xb8
-  __DATA_CONST.__objc_superrefs: 0x4010
+  __DATA_CONST.__objc_superrefs: 0x4018
   __DATA_CONST.__objc_arraydata: 0x1870
   __AUTH_CONST.__auth_got: 0x2ae8
   __AUTH_CONST.__const: 0x10258
-  __AUTH_CONST.__cfstring: 0x70520
-  __AUTH_CONST.__objc_const: 0x26f600
+  __AUTH_CONST.__cfstring: 0x70540
+  __AUTH_CONST.__objc_const: 0x26f6b8
   __AUTH_CONST.__objc_arrayobj: 0x1770
   __AUTH_CONST.__objc_doubleobj: 0x790
   __AUTH_CONST.__objc_intobj: 0x2cb8
   __AUTH_CONST.__objc_dictobj: 0x320
-  __AUTH.__objc_data: 0x108b0
-  __DATA.__objc_ivar: 0xf70c
+  __AUTH.__objc_data: 0x10900
+  __DATA.__objc_ivar: 0xf710
   __DATA.__data: 0x1fb08
   __DATA.__bss: 0xac0
   __DATA.__common: 0xa48

   - /usr/lib/libsp.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libutil.dylib
-  Functions: 71513
-  Symbols:   241908
-  CStrings:  105382
+  Functions: 71515
+  Symbols:   241919
+  CStrings:  105387
 
Sections:
~ __TEXT.__init_offsets : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __TEXT.__unwind_info : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_nlcatlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_doubleobj : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
Symbols:
+ -[SBUntrustedURLLaunchThrottle .cxx_destruct]
+ -[SBUntrustedURLLaunchThrottle _shouldThrottleRequestForRequestedBundleID:atTime:]
+ -[SBUntrustedURLLaunchThrottle init]
+ -[SBUntrustedURLLaunchThrottle shouldThrottleRequestForRequestedBundleID:options:]
+ GCC_except_table169
+ GCC_except_table377
+ _OBJC_CLASS_$_SBUntrustedURLLaunchThrottle
+ _OBJC_IVAR_$_SBMainWorkspace._untrustedURLLaunchThrottle
+ _OBJC_IVAR_$_SBUntrustedURLLaunchThrottle._entries
+ _OBJC_METACLASS_$_SBUntrustedURLLaunchThrottle
+ __OBJC_$_INSTANCE_METHODS_SBUntrustedURLLaunchThrottle
+ __OBJC_$_INSTANCE_VARIABLES_SBUntrustedURLLaunchThrottle
+ __OBJC_CLASS_RO_$_SBUntrustedURLLaunchThrottle
+ __OBJC_METACLASS_RO_$_SBUntrustedURLLaunchThrottle
+ _objc_msgSend$_shouldThrottleRequestForRequestedBundleID:atTime:
+ _objc_msgSend$shouldThrottleRequestForRequestedBundleID:options:
- -[SBMainWorkspace _shouldThrottleUntrustedURLLaunchForApplication:options:]
- -[SBMainWorkspace _untrustedURLLaunchRequestWindowEntryForBundleID:atTime:]
- GCC_except_table141
- GCC_except_table173
- _OBJC_IVAR_$_SBMainWorkspace._untrustedURLLaunchRequestWindowEntries
- _objc_msgSend$_shouldThrottleUntrustedURLLaunchForApplication:options:
- _objc_msgSend$_untrustedURLLaunchRequestWindowEntryForBundleID:atTime:
CStrings:
+ "<unknown_requested_bundle_id>"
+ "@\"SBUntrustedURLLaunchThrottle\""
+ "SBUntrustedURLLaunchThrottle"
+ "Throttled untrusted URL request from origin=%{public}@, requestedBundleID=%{public}@"
+ "_entries"
+ "_shouldThrottleRequestForRequestedBundleID:atTime:"
+ "_untrustedURLLaunchThrottle"
+ "shouldThrottleRequestForRequestedBundleID:options:"
- "Throttled untrusted URL request from %{public}@"
- "_shouldThrottleUntrustedURLLaunchForApplication:options:"
- "_untrustedURLLaunchRequestWindowEntries"
- "_untrustedURLLaunchRequestWindowEntryForBundleID:atTime:"

```
