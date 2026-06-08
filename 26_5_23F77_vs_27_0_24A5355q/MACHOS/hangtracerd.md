## hangtracerd

> `/usr/libexec/hangtracerd`

```diff

-398.2.0.0.0
-  __TEXT.__text: 0x34d1c
-  __TEXT.__auth_stubs: 0xed0
-  __TEXT.__objc_stubs: 0x5580
-  __TEXT.__objc_methlist: 0x20e4
-  __TEXT.__const: 0x3f8
-  __TEXT.__gcc_except_tab: 0x3ac
-  __TEXT.__objc_methname: 0x8abd
-  __TEXT.__cstring: 0x4970
-  __TEXT.__objc_classname: 0x32a
-  __TEXT.__objc_methtype: 0x1071
-  __TEXT.__oslogstring: 0x6490
-  __TEXT.__unwind_info: 0xb08
-  __DATA_CONST.__auth_got: 0x778
-  __DATA_CONST.__got: 0x440
-  __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x1fa0
-  __DATA_CONST.__cfstring: 0x5fe0
-  __DATA_CONST.__objc_classlist: 0xf0
+412.0.0.0.0
+  __TEXT.__text: 0x35a04
+  __TEXT.__auth_stubs: 0xf90
+  __TEXT.__objc_stubs: 0x5b20
+  __TEXT.__objc_methlist: 0x27ec
+  __TEXT.__const: 0x3e8
+  __TEXT.__cstring: 0x4cb0
+  __TEXT.__objc_methname: 0x9945
+  __TEXT.__objc_classname: 0x37d
+  __TEXT.__objc_methtype: 0x1305
+  __TEXT.__gcc_except_tab: 0x3c4
+  __TEXT.__oslogstring: 0x66ea
+  __TEXT.__unwind_info: 0xb48
+  __DATA_CONST.__const: 0x20d8
+  __DATA_CONST.__cfstring: 0x63c0
+  __DATA_CONST.__objc_classlist: 0x128
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0xa0
+  __DATA_CONST.__objc_superrefs: 0xd8
   __DATA_CONST.__objc_intobj: 0x90
+  __DATA_CONST.__objc_doubleobj: 0x30
   __DATA_CONST.__objc_arraydata: 0x90
-  __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__objc_dictobj: 0x78
-  __DATA.__objc_const: 0x4ad0
-  __DATA.__objc_selrefs: 0x1b30
-  __DATA.__objc_ivar: 0x43c
-  __DATA.__objc_data: 0x960
-  __DATA.__data: 0x540
-  __DATA.__bss: 0x548
+  __DATA_CONST.__objc_arrayobj: 0x18
+  __DATA_CONST.__auth_got: 0x7d8
+  __DATA_CONST.__got: 0x448
+  __DATA_CONST.__auth_ptr: 0x10
+  __DATA.__objc_const: 0x5938
+  __DATA.__objc_selrefs: 0x1e80
+  __DATA.__objc_ivar: 0x508
+  __DATA.__objc_data: 0xb90
+  __DATA.__data: 0x548
+  __DATA.__bss: 0x560
   __DATA.__common: 0x70
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  UUID: 11D16BC7-CBB2-3BE5-A90C-025DD83C4B4C
-  Functions: 1196
-  Symbols:   388
-  CStrings:  3672
+  UUID: E29956B2-9F29-3080-AFB5-5ED7856266CF
+  Functions: 1357
+  Symbols:   401
+  CStrings:  3967
 
Symbols:
+ _CGColorGetAlpha
+ _CGColorRelease
+ _NSStringFromClass
+ _NSStringFromSelector
+ _OBJC_CLASS_$_BSMachPortSendRight
+ _mach_continuous_time
+ _memcpy
+ _notify_cancel
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x3
+ _objc_retain_x6
+ _strncpy
+ _strnlen
- _objc_retainAutoreleasedReturnValue
CStrings:
+ " No HUD lines to clear, hiding container layer."
+ "%.1f"
+ "%@ %@"
+ "(nil)"
+ "<%@: %p lineID=%llu type=%@ op=%@ title=\"%@\" label=\"%@\" %@ color=%@ staticColor=%@ thresholdMet=%@ displayThreshold=%lld thresholdDir=%@ timeoutMS=%u overflowValue=%u flags=0x%x receivedTimestamp=%llu (%.0fms ago) lastUpdateTimestamp=%llu (%.0fms ago) writeTimestamp=%llu clientProvidedTimestamp=%llu>"
+ "<="
+ ">="
+ "@\"BSMachPortSendRight\""
+ "@\"PerfHUDAnimatedValueLayer\""
+ "@\"PerfHUDKeyLayer\""
+ "@\"PerfHUDLineConfig\""
+ "@\"PerfHUDValueLayer\""
+ "@288@0:8{?=QCCCC[4C]QQIIqC[7C][3{?=qC[7C]}]CC[6C]C[7C](?=[56c]qdQ)[8c][32c][48c]CC[6C]}16"
+ "@36@0:8B16@20@28"
+ "@48@0:8@16@24d32@40"
+ "@56@0:8@16@24@32d40d48"
+ "A new PerfHUD line is created with title=%@ label=%@ value=%@ with lineID %llu. contentId:%@"
+ "B28@0:8@16B24"
+ "C24@0:8q16"
+ "Failed to create NSString for HUD from bundleID: %s"
+ "HangHUDClient does not support PerfHUDs"
+ "HangTracerEnableHUDClients"
+ "HangTracerHUDOpacity"
+ "PerfHUD"
+ "PerfHUDAnimatedValueLayer"
+ "PerfHUDClientConfiguration"
+ "PerfHUDConnectionResponse"
+ "PerfHUDKeyLayer"
+ "PerfHUDLine %llu (one-shot) finished updates, no fade"
+ "PerfHUDLine %llu finished updates, starting fade-out"
+ "PerfHUDLine %llu reactivating from faded state"
+ "PerfHUDLine %llu: animation in progress, skipping update"
+ "PerfHUDLineState"
+ "PerfHUDServerLine"
+ "PerfHUDValueLayer"
+ "Q32@0:8@16Q24"
+ "T@\"BSMachPortSendRight\",R,N,V_sharedMemoryPort"
+ "T@\"CATextLayer\",R,N,V_labelLayer"
+ "T@\"CATextLayer\",R,N,V_titleLayer"
+ "T@\"CATextLayer\",R,N,V_unitLayer"
+ "T@\"CATextLayer\",R,N,V_valueTextLayer"
+ "T@\"NSDictionary\",C,N,V_selectedValues"
+ "T@\"NSString\",C,N,V_label"
+ "T@\"NSString\",C,N,V_stringValue"
+ "T@\"NSString\",C,N,V_title"
+ "T@\"NSString\",C,N,V_unit"
+ "T@\"PerfHUDAnimatedValueLayer\",R,N,V_perfAnimatedValueLayer"
+ "T@\"PerfHUDKeyLayer\",R,N,V_perfKeyLayer"
+ "T@\"PerfHUDLineConfig\",C,N,V_lineConfig"
+ "T@\"PerfHUDValueLayer\",R,N,V_perfValueLayer"
+ "TB,N,V_clientEnabled"
+ "TB,N,V_thresholdMet"
+ "TB,R,N"
+ "TB,R,V_areHUDClientsEnabled"
+ "TC,N,V_colorThresholdCount"
+ "TC,N,V_currentColor"
+ "TC,N,V_flags"
+ "TC,N,V_lineType"
+ "TC,N,V_operation"
+ "TC,N,V_staticColor"
+ "TC,N,V_thresholdDirection"
+ "TC,N,V_valueType"
+ "TI,N,V_overflowValue"
+ "TI,N,V_timeoutMS"
+ "TI,R,V_hudOpacityLevel"
+ "TQ,N,V_clientProvidedTimestamp"
+ "TQ,N,V_eventStart"
+ "TQ,N,V_lastUpdateTimestamp"
+ "TQ,N,V_lineID"
+ "TQ,N,V_receivedTimestamp"
+ "TQ,N,V_timeValue"
+ "TQ,N,V_writeTimestamp"
+ "Td,N,V_currentValue"
+ "Td,N,V_floatValue"
+ "Tq,N,V_displayThreshold"
+ "Tq,N,V_intValue"
+ "Tr^{?=qC[7C]},R,N"
+ "[3{?=\"threshold\"q\"color\"C\"_pad\"[7C]}]"
+ "^{CGColor=}24@0:8@16"
+ "_animationLock"
+ "_areHUDClientsEnabled"
+ "_clientEnabled"
+ "_clientProvidedTimestamp"
+ "_colorThresholdCount"
+ "_colorThresholds"
+ "_currentColor"
+ "_currentValue"
+ "_displayThreshold"
+ "_eventStart"
+ "_flags"
+ "_floatValue"
+ "_hudOpacityLevel"
+ "_intValue"
+ "_label"
+ "_labelLayer"
+ "_lastUpdateTimestamp"
+ "_lineConfig"
+ "_lineID"
+ "_lineType"
+ "_lockedClearAnimation"
+ "_lockedGetAnimation"
+ "_lockedSetAnimation:"
+ "_opacityNotifyToken"
+ "_operation"
+ "_overflowValue"
+ "_perfAnimatedValueLayer"
+ "_perfKeyLayer"
+ "_perfValueLayer"
+ "_selectedValues"
+ "_sharedMemoryPort"
+ "_spaceBetweenLayers"
+ "_staticColor"
+ "_stringValue"
+ "_thresholdDirection"
+ "_thresholdMet"
+ "_timeValue"
+ "_timeoutMS"
+ "_title"
+ "_titleLayer"
+ "_unit"
+ "_unitLayer"
+ "_userBackgroundOpacity"
+ "_valueTextLayer"
+ "_valueType"
+ "_writeTimestamp"
+ "applyBackgroundOpacity"
+ "areHUDClientsEnabled"
+ "bitmaskValueForKey:defaultValue:"
+ "boolValueForKey:defaultValue:"
+ "class_name"
+ "clientEnabled"
+ "clientProvidedTimestamp"
+ "colorForLineState:"
+ "colorThresholdCount"
+ "colorThresholds"
+ "com.apple.HangHUD.HUDUpdateQueue"
+ "com.apple.da.hud_layer_refresh"
+ "com.apple.hangtracer.prefs_type_mismatch"
+ "computeColorForValue:"
+ "connectPerfHUDClientWithBundleID:clientID:completion:"
+ "critical"
+ "currentColor"
+ "currentValue"
+ "currentValueAtTime:"
+ "displayThreshold"
+ "end"
+ "eventStart"
+ "eventStart=%llu timeValue=%llu"
+ "expected_selector"
+ "f"
+ "filters"
+ "flags"
+ "float=%.2f%@"
+ "floatValue"
+ "handleCompletionWithLineState:"
+ "handleReactivationWithLineState:"
+ "hudOpacityLevel"
+ "initPropertyAreHUDClientsEnabled:"
+ "initPropertyHUDOpacity:"
+ "initWithClientEnabled:lineConfig:selectedValues:"
+ "initWithEntry:"
+ "initWithLineState:theme:fontSize:lineDelegate:"
+ "initWithSharedMemoryPort:"
+ "initWithTitle:label:theme:fontSize:contentScale:"
+ "initWithValueText:unit:theme:"
+ "int=%lld%@"
+ "integerValueForKey:defaultValue:"
+ "key_name"
+ "label"
+ "labelFadeIn"
+ "labelLayer"
+ "lastUpdateTimestamp"
+ "lineConfig"
+ "lineID"
+ "lineKey"
+ "lineType"
+ "markAsEnded"
+ "normal"
+ "oneshot"
+ "operation"
+ "overflowIndicatesTimeout"
+ "overflowValue"
+ "perfAnimatedValueLayer"
+ "perfKeyLayer"
+ "perfValueLayer"
+ "populateFromEntry:"
+ "q24@0:8Q16"
+ "q32@0:8@16q24"
+ "r^{?=qC[7C]}16@0:8"
+ "receivePerfHUDConnectionWithBundleID:clientID:completion:"
+ "removeAnimationForKey:"
+ "selectedValues"
+ "setAnimationDuration:"
+ "setClientEnabled:"
+ "setClientProvidedTimestamp:"
+ "setColorThresholdCount:"
+ "setCurrentColor:"
+ "setCurrentValue:"
+ "setDisplayThreshold:"
+ "setEventStart:"
+ "setFilters:"
+ "setFlags:"
+ "setFloatValue:"
+ "setIntValue:"
+ "setLabel:"
+ "setLastUpdateTimestamp:"
+ "setLineConfig:"
+ "setLineID:"
+ "setLineType:"
+ "setOperation:"
+ "setOverflowValue:"
+ "setReceivedTimestamp:"
+ "setSelectedValues:"
+ "setStaticColor:"
+ "setStringValue:"
+ "setThresholdDirection:"
+ "setThresholdMet:"
+ "setTimeValue:"
+ "setTimeoutMS:"
+ "setUnit:"
+ "setValue:animated:"
+ "setValueType:"
+ "setWriteTimestamp:"
+ "settings-navigation://com.apple.Settings.Internal.Classic/HangTracerHUDSettings/"
+ "severe"
+ "sharedMemoryPort"
+ "shouldInterpolate"
+ "shouldShowOverflow"
+ "staticColor"
+ "stream"
+ "string=\"%@\""
+ "stringSetForKey:"
+ "stringValue"
+ "thresholdDirection"
+ "thresholdMet"
+ "timeValue"
+ "timeoutMS"
+ "title"
+ "titleLayer"
+ "type_mismatch"
+ "unit"
+ "unitLayer"
+ "unknown"
+ "update"
+ "updateValueLayersWithLineState:"
+ "updateWithEntry:"
+ "updateWithEntry: after update lineID=%llu title=\"%@\" label=\"%@\" timeValue=%llu eventStart=%llu"
+ "updateWithEntry: lineID=%llu op=%@ hasContent=%@ titleLen=%u labelLen=%u valueType=%d timeValue=%llu"
+ "updateWithEntry: skipping content update for PerfOpEnd with no content"
+ "updateWithTitle:color:"
+ "updateWithTitle:label:color:theme:fontSize:contentScale:"
+ "updateWithValueText:color:"
+ "v20@0:8C16"
+ "v20@0:8I16"
+ "v288@0:8{?=QCCCC[4C]QQIIqC[7C][3{?=qC[7C]}]CC[6C]C[7C](?=[56c]qdQ)[8c][32c][48c]CC[6C]}16"
+ "v32@0:8@16^{CGColor=}24"
+ "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"PerfHUDConnectionResponse\"@\"NSError\">32"
+ "v64@0:8@16@24^{CGColor=}32@40d48d56"
+ "value"
+ "valueForKey:"
+ "valueTextForLineState:"
+ "valueTextLayer"
+ "valueType"
+ "writeTimestamp"
+ "\xf1C"
- " Invalid HUD line clear request found. The number of HUD lines is 0."
- "settings-navigation://com.apple.Settings.Internal.Classic/HANGTRACER/"

```
