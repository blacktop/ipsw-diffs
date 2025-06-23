## PerfPowerMetricMonitor

> `/System/Library/PrivateFrameworks/PerfPowerMetricMonitor.framework/PerfPowerMetricMonitor`

```diff

-2954.0.0.502.3
-  __TEXT.__text: 0x17190
-  __TEXT.__auth_stubs: 0x570
-  __TEXT.__objc_methlist: 0x13dc
+2964.0.40.502.1
+  __TEXT.__text: 0x178fc
+  __TEXT.__auth_stubs: 0x5b0
+  __TEXT.__objc_methlist: 0x142c
   __TEXT.__const: 0x110
-  __TEXT.__gcc_except_tab: 0x844
-  __TEXT.__cstring: 0x17cb
-  __TEXT.__oslogstring: 0x147d
+  __TEXT.__gcc_except_tab: 0x86c
+  __TEXT.__cstring: 0x189b
+  __TEXT.__oslogstring: 0x1594
   __TEXT.__ustring: 0x6c0
-  __TEXT.__unwind_info: 0x4a8
+  __TEXT.__unwind_info: 0x4b0
   __TEXT.__objc_classname: 0x185
-  __TEXT.__objc_methname: 0x3998
+  __TEXT.__objc_methname: 0x3ac0
   __TEXT.__objc_methtype: 0x660
-  __TEXT.__objc_stubs: 0x2f00
-  __DATA_CONST.__got: 0xe8
+  __TEXT.__objc_stubs: 0x3000
+  __DATA_CONST.__got: 0xf0
   __DATA_CONST.__const: 0x5c0
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xda0
+  __DATA_CONST.__objc_selrefs: 0xde0
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x40
-  __DATA_CONST.__objc_arraydata: 0x208
-  __AUTH_CONST.__auth_got: 0x2c8
+  __DATA_CONST.__objc_arraydata: 0x220
+  __AUTH_CONST.__auth_got: 0x2e8
   __AUTH_CONST.__const: 0x160
-  __AUTH_CONST.__cfstring: 0x1220
-  __AUTH_CONST.__objc_const: 0x1fa8
+  __AUTH_CONST.__cfstring: 0x12c0
+  __AUTH_CONST.__objc_const: 0x2038
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0x1e4
+  __DATA.__objc_ivar: 0x1f0
   __DATA.__data: 0x300
   __DATA.__bss: 0x50
   __DATA_DIRTY.__objc_data: 0x280

   - /System/Library/PrivateFrameworks/AssertionServices.framework/AssertionServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1AE5B681-90CF-30BF-8B1A-57BBD87463EA
-  Functions: 558
-  Symbols:   1959
-  CStrings:  1229
+  UUID: EF7DA862-EE01-3701-B90D-ED1929583860
+  Functions: 567
+  Symbols:   1994
+  CStrings:  1255
 
Symbols:
+ -[PPSMetricMonitorService _canStartMonitoringForClient:withError:].cold.4
+ -[PPSMetricMonitorService _hasEntitlements:]
+ -[PPSMetricMonitorService _hasEntitlements:].cold.1
+ -[PPSProcessMetricCollection qosDefault]
+ -[PPSProcessMetricCollection qosMaintenance]
+ -[PPSProcessMetricCollection qosUnspecified]
+ -[PPSProcessMetricCollection setQosDefault:]
+ -[PPSProcessMetricCollection setQosMaintenance:]
+ -[PPSProcessMetricCollection setQosUnspecified:]
+ GCC_except_table105
+ GCC_except_table177
+ _OBJC_EHTYPE_$_NSException
+ _OBJC_IVAR_$_PPSProcessMetricCollection._qosDefault
+ _OBJC_IVAR_$_PPSProcessMetricCollection._qosMaintenance
+ _OBJC_IVAR_$_PPSProcessMetricCollection._qosUnspecified
+ ___block_literal_global.274
+ ___block_literal_global.278
+ _dispatch_walltime
+ _objc_begin_catch
+ _objc_end_catch
+ _objc_msgSend$_hasEntitlements:
+ _objc_msgSend$qosDefault
+ _objc_msgSend$qosMaintenance
+ _objc_msgSend$qosUnspecified
+ _objc_msgSend$setQosDefault:
+ _objc_msgSend$setQosMaintenance:
+ _objc_msgSend$setQosUnspecified:
+ _objc_msgSend$valueForEntitlement:
+ _objc_retainAutoreleasedReturnValue
- GCC_except_table175
- ___block_literal_global.271
- ___block_literal_global.275
CStrings:
+ "Energy Cost        %8.3f     %@\nEnergy Overhead    %8.3f     %@\nCPU Cost           %8.3f     %@\nCPU Seconds        %8.3f s   %@\nCPU Energy         %8.3f nJ  %@\nGPU Cost           %8.3f     %@\nDisplay Power      %8.3f     %@\nNetwork Cost       %8d     %@\nWiFi In            %8d B   %@\nWiFi Out           %8d B   %@\nCell In            %8d B   %@\nCell Out           %8d B   %@\nLocation Cost      %8.3f     %@\nOngoing Location   %8s     %@\nLocation Desired Accuracy %8.3f %@\nQOS Utility %8.3f s   %@\nQOS Background %8.3f s   %@\nQOS User Initiated %8.3f s   %@\nQOS User Interactive %8.3f s   %@\nQOS Default %8.3f s   %@\nQOS Maintenance %8.3f s   %@\nQOS Unspecified %8.3f s   %@\nApplication State               %@\n%29s"
+ "Exception occurred when doing an Entitlement Check: %@"
+ "Headless client is missing entitlement"
+ "Missing headless client entitlement"
+ "Process name: %{public}s\nSignpost ID is PID\nCPU Power Impact = %{public, name=CPU_Power_Impact}.2f\nGPU Power Impact = %{public, name=GPU_Power_Impact}.2f\nQOS Utility = %{public, name=QOS_Utility, units=s}.2f s\nQOS Background = %{public, name=QOS_Background, units=s}.2f s\nQOS User Initiated = %{public, name=QOS_User_Initiated, units=s}.2f s\nQOS User Interactive = %{public, name=QOS_User_Interactive, units=s}.2f s\nCPU Instructions = %{public, name=CPU_Instructions}lld \nANE Time = %{public, name=ANE_Time, units=s}.2f s \nLocation Desired Accuracy = %{public, name=Location_Desired_Accuracy}.2f \nApplication State = %{public, name=Application_State}d \nDisplay Power Impact = %{public, name=Display_Power_Impact}.2f\n%{public, signpost.description:begin_time}llu\n%{public, signpost.description:end_time}llu\nQOS Default = %{public, name=QOS_Default, units=s}.2f s\nQOS Maintenance = %{public, name=QOS_Maintenance, units=s}.2f s\nQOS Unspecified = %{public, name=QOS_Unspecified, units=s}.2f s\n"
+ "T@\"PPSMetricSample\",&,N,V_qosDefault"
+ "T@\"PPSMetricSample\",&,N,V_qosMaintenance"
+ "T@\"PPSMetricSample\",&,N,V_qosUnspecified"
+ "Trimmed %lu old sleep/wake intervals."
+ "_hasEntitlements:"
+ "_qosDefault"
+ "_qosMaintenance"
+ "_qosUnspecified"
+ "com.apple.PerfPowerMetricMonitorHeadless.client"
+ "qosDefault"
+ "qosMaintenance"
+ "qosUnspecified"
+ "setQosDefault:"
+ "setQosMaintenance:"
+ "setQosUnspecified:"
+ "valueForEntitlement:"
- "Energy Cost        %8.3f     %@\nEnergy Overhead    %8.3f     %@\nCPU Cost           %8.3f     %@\nCPU Seconds        %8.3f s   %@\nCPU Energy         %8.3f nJ  %@\nGPU Cost           %8.3f     %@\nDisplay Power      %8.3f     %@\nNetwork Cost       %8d     %@\nWiFi In            %8d B   %@\nWiFi Out           %8d B   %@\nCell In            %8d B   %@\nCell Out           %8d B   %@\nLocation Cost      %8.3f     %@\nOngoing Location   %8s     %@\nLocation Desired Accuracy %8.3f %@\nQOS Utility %8.3f s   %@\nQOS Background %8.3f s   %@\nQOS User Initiated %8.3f s   %@\nQOS User Interactive %8.3f s   %@\nApplication State               %@\n%29s"
- "Process name: %{public}s\nSignpost ID is PID\nCPU Power Impact = %{public, name=CPU_Power_Impact}.2f\nGPU Power Impact = %{public, name=GPU_Power_Impact}.2f\nQOS Utility = %{public, name=QOS_Utility, units=s}.2f s\nQOS Background = %{public, name=QOS_Background, units=s}.2f s\nQOS User Initiated = %{public, name=QOS_User_Initiated, units=s}.2f s\nQOS User Interactive = %{public, name=QOS_User_Interactive, units=s}.2f s\nCPU Instructions = %{public, name=CPU_Instructions}lld \nANE Time = %{public, name=ANE_Time, units=s}.2f s \nLocation Desired Accuracy = %{public, name=Location_Desired_Accuracy}.2f \nApplication State = %{public, name=Application_State}d \nDisplay Power Impact = %{public, name=Display_Power_Impact}.2f\n%{public, signpost.description:begin_time}llu\n%{public, signpost.description:end_time}llu\n"
- "Trimed %lu old sleep/wake intervals."

```
