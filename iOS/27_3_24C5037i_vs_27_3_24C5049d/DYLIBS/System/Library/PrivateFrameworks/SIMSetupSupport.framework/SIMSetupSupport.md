## SIMSetupSupport

> `/System/Library/PrivateFrameworks/SIMSetupSupport.framework/SIMSetupSupport`

```diff

-983.0.0.0.0
-  __TEXT.__text: 0xe3a18
-  __TEXT.__objc_methlist: 0xc82c
+984.1.0.0.0
+  __TEXT.__text: 0xe561c
+  __TEXT.__objc_methlist: 0xc904
   __TEXT.__const: 0x1f0
-  __TEXT.__gcc_except_tab: 0x218c
-  __TEXT.__cstring: 0x179ce
-  __TEXT.__oslogstring: 0x8ca3
-  __TEXT.__dlopen_cstrs: 0x2be
+  __TEXT.__gcc_except_tab: 0x2220
+  __TEXT.__cstring: 0x17cd0
+  __TEXT.__oslogstring: 0x8dfc
+  __TEXT.__dlopen_cstrs: 0x308
   __TEXT.__ustring: 0xa
-  __TEXT.__unwind_info: 0x3f70
+  __TEXT.__unwind_info: 0x4010
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2130
-  __DATA_CONST.__objc_classlist: 0x590
+  __DATA_CONST.__const: 0x21b8
+  __DATA_CONST.__objc_classlist: 0x598
   __DATA_CONST.__objc_catlist: 0x70
   __DATA_CONST.__objc_protolist: 0x118
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5f88
+  __DATA_CONST.__objc_selrefs: 0x6030
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x530
+  __DATA_CONST.__objc_superrefs: 0x538
   __DATA_CONST.__objc_arraydata: 0x228
-  __DATA_CONST.__got: 0xc18
-  __AUTH_CONST.__const: 0xbc0
-  __AUTH_CONST.__cfstring: 0xade0
-  __AUTH_CONST.__objc_const: 0x4f918
-  __AUTH_CONST.__objc_intobj: 0x7f8
+  __DATA_CONST.__got: 0xc40
+  __AUTH_CONST.__const: 0xbe0
+  __AUTH_CONST.__cfstring: 0xae40
+  __AUTH_CONST.__objc_const: 0x4fad0
+  __AUTH_CONST.__objc_intobj: 0x828
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x36b0
-  __DATA.__objc_ivar: 0x1360
+  __AUTH.__objc_data: 0x3700
+  __DATA.__objc_ivar: 0x1380
   __DATA.__data: 0xd30
   __DATA_DIRTY.__objc_data: 0xf0
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 4979
-  Symbols:   8004
-  CStrings:  3148
+  Functions: 5011
+  Symbols:   8053
+  CStrings:  3165
 
Symbols:
+ -[SSQuickSwitchWaitOnWebsheetViewController _groupedCode:]
+ -[SSQuickSwitchWaitOnWebsheetViewController _highLegibilityCodeFont]
+ -[SSQuickSwitchWaitOnWebsheetViewController initWithPlanInfos:isQuickSwitchSlidingOngoing:isOneTimeCodeExpected:]
+ -[SSQuickSwitchWaitOnWebsheetViewController showOneTimeCode:]
+ -[TSCellularPlanActivatingFlow isWebsheetOneTimeCodeExpected]
+ -[TSCellularPlanActivatingFlow setIsWebsheetOneTimeCodeExpected:]
+ -[TSCellularPlanActivatingFlow setWebsheetOneTimeCodeMonitor:]
+ -[TSCellularPlanActivatingFlow websheetOneTimeCodeMonitor]
+ -[TSCellularPlanActivatingFlow(CoreTelephonyClientQuickSwitchEnrollmentDelegate) _isWebsheetOneTimeCodeEnabledByCarrier:]
+ -[TSCellularPlanActivatingFlow(CoreTelephonyClientQuickSwitchEnrollmentDelegate) _maybeStartWebsheetOneTimeCodeMonitor:]
+ -[TSCellularPlanActivatingFlow(CoreTelephonyClientQuickSwitchEnrollmentDelegate) _startWebsheetOneTimeCodeMonitor]
+ -[TSCellularPlanActivatingFlow(CoreTelephonyClientQuickSwitchEnrollmentDelegate) _stopWebsheetOneTimeCodeMonitor]
+ -[TSOneTimeCodeMonitor .cxx_destruct]
+ -[TSOneTimeCodeMonitor _report:timestamp:handler:]
+ -[TSOneTimeCodeMonitor initWithAcceleratorFactory:]
+ -[TSOneTimeCodeMonitor init]
+ -[TSOneTimeCodeMonitor startWithHandler:]
+ -[TSOneTimeCodeMonitor stop]
+ GCC_except_table137
+ GCC_except_table143
+ GCC_except_table149
+ GCC_except_table157
+ GCC_except_table158
+ GCC_except_table165
+ GCC_except_table170
+ GCC_except_table172
+ GCC_except_table174
+ GCC_except_table181
+ GCC_except_table215
+ GCC_except_table226
+ GCC_except_table228
+ GCC_except_table230
+ _OBJC_CLASS_$_TSOneTimeCodeMonitor
+ _OBJC_IVAR_$_SSQuickSwitchWaitOnWebsheetViewController._oneTimeCodeLabel
+ _OBJC_IVAR_$_TSCellularPlanActivatingFlow._isWebsheetOneTimeCodeExpected
+ _OBJC_IVAR_$_TSCellularPlanActivatingFlow._websheetOneTimeCodeMonitor
+ _OBJC_IVAR_$_TSOneTimeCodeMonitor._accelerator
+ _OBJC_IVAR_$_TSOneTimeCodeMonitor._acceleratorFactory
+ _OBJC_IVAR_$_TSOneTimeCodeMonitor._reportedCodes
+ _OBJC_IVAR_$_TSOneTimeCodeMonitor._startTime
+ _OBJC_IVAR_$_TSOneTimeCodeMonitor._started
+ _OBJC_METACLASS_$_TSOneTimeCodeMonitor
+ _OUTLINED_FUNCTION_7
+ _UIFontDescriptorFeatureSettingsAttribute
+ _UIFontFeatureSelectorIdentifierKey
+ _UIFontFeatureTypeIdentifierKey
+ _UIFontWeightBold
+ __OBJC_$_INSTANCE_METHODS_TSOneTimeCodeMonitor
+ __OBJC_$_INSTANCE_VARIABLES_TSOneTimeCodeMonitor
+ __OBJC_CLASS_RO_$_TSOneTimeCodeMonitor
+ __OBJC_METACLASS_RO_$_TSOneTimeCodeMonitor
+ ___114-[TSCellularPlanActivatingFlow(CoreTelephonyClientQuickSwitchEnrollmentDelegate) _startWebsheetOneTimeCodeMonitor]_block_invoke
+ ___116-[TSCellularPlanActivatingFlow(CoreTelephonyClientQuickSwitchEnrollmentDelegate) updateQuickSwitchEnrollmentStatus:]_block_invoke
+ ___120-[TSCellularPlanActivatingFlow(CoreTelephonyClientQuickSwitchEnrollmentDelegate) _maybeStartWebsheetOneTimeCodeMonitor:]_block_invoke
+ ___121-[TSCellularPlanActivatingFlow(CoreTelephonyClientQuickSwitchEnrollmentDelegate) _isWebsheetOneTimeCodeEnabledByCarrier:]_block_invoke
+ ___28-[TSOneTimeCodeMonitor init]_block_invoke
+ ___41-[TSOneTimeCodeMonitor startWithHandler:]_block_invoke
+ ___41-[TSOneTimeCodeMonitor startWithHandler:]_block_invoke_2
+ ___block_descriptor_32_e24_16?0?<v?"NSArray">8l
+ ___block_descriptor_56_e8_32s40bs48w_e50_v24?0"CTXPCServiceSubscriptionInfo"8"NSError"16lw48l8s32l8s40l8
+ ___block_descriptor_56_e8_32s40bs48w_e5_v8?0ls32l8w48l8s40l8
- -[SSQuickSwitchWaitOnWebsheetViewController initWithPlanInfos:isQuickSwitchSlidingOngoing:]
- GCC_except_table133
- GCC_except_table135
- GCC_except_table145
- GCC_except_table153
- GCC_except_table154
- GCC_except_table161
- GCC_except_table169
- GCC_except_table203
- GCC_except_table206
- GCC_except_table214
- GCC_except_table216
CStrings:
+ "-[SSQuickSwitchWaitOnWebsheetViewController showOneTimeCode:]"
+ "-[TSCellularPlanActivatingFlow(CoreTelephonyClientQuickSwitchEnrollmentDelegate) _isWebsheetOneTimeCodeEnabledByCarrier:]"
+ "-[TSCellularPlanActivatingFlow(CoreTelephonyClientQuickSwitchEnrollmentDelegate) _isWebsheetOneTimeCodeEnabledByCarrier:]_block_invoke"
+ "-[TSCellularPlanActivatingFlow(CoreTelephonyClientQuickSwitchEnrollmentDelegate) _maybeStartWebsheetOneTimeCodeMonitor:]_block_invoke"
+ "-[TSCellularPlanActivatingFlow(CoreTelephonyClientQuickSwitchEnrollmentDelegate) _startWebsheetOneTimeCodeMonitor]_block_invoke"
+ "-[TSOneTimeCodeMonitor _report:timestamp:handler:]"
+ "-[TSOneTimeCodeMonitor startWithHandler:]"
+ "@16@?0@?<v@?@\"NSArray\">8"
+ "OneTimeCodeInWebsheet"
+ "QS_SLIDING_VERIFICATION_CODE_WILL_APPEAR_DETAILS"
+ "[E]no subscription context for quick switch plan %@ @%s"
+ "[E]subscription %@ not found: %@ @%s"
+ "captured websheet one time code, current VC: %@ @%s"
+ "ignoring one time code older than monitoring start (timestamp: %@) @%s"
+ "monitoring SMS for one time codes @%s"
+ "showing websheet one time code @%s"
+ "websheet one time code enabled by carrier: %{bool}d @%s"
+ "\xf0D\xe1"
- "\xf04\xe1"
```
