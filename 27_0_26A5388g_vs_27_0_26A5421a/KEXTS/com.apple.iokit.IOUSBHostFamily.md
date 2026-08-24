## com.apple.iokit.IOUSBHostFamily

> `com.apple.iokit.IOUSBHostFamily`

```diff

-1617.0.9.0.0
-  __TEXT.__cstring: 0xa41b
-  __TEXT.__os_log: 0x8717
+1617.0.12.0.0
+  __TEXT.__cstring: 0xa478
+  __TEXT.__os_log: 0x873b
   __TEXT.__const: 0x2018
-  __TEXT_EXEC.__text: 0x9ac18
+  __TEXT_EXEC.__text: 0x9b190
   __TEXT_EXEC.__auth_stubs: 0xd50
   __DATA.__data: 0x1f0
   __DATA.__common: 0x970
   __DATA.__bss: 0x10
   __DATA_CONST.__mod_init_func: 0xf0
   __DATA_CONST.__mod_term_func: 0xe8
-  __DATA_CONST.__const: 0x14a60
-  __DATA_CONST.__kalloc_type: 0x1b80
+  __DATA_CONST.__const: 0x14a88
+  __DATA_CONST.__kalloc_type: 0x1d80
   __DATA_CONST.__kalloc_var: 0x280
   __DATA_CONST.__auth_got: 0x6a8
   __DATA_CONST.__got: 0x1f0
-  Functions: 2334
-  Symbols:   4169
-  CStrings:  1156
+  Functions: 2337
+  Symbols:   4175
+  CStrings:  1160
 
Symbols:
+ __ZN16AppleUSBHostPort26terminateServiceThreadCallEPNS_30tPortTerminateServiceArgumentsEP11thread_call
+ __ZZN15IOUSBHostDevice23AsyncDeviceRequest_ImplEP9IOServicehhtttP18IOMemoryDescriptorP8OSActionjE21kalloc_type_view_5983
+ __ZZN15IOUSBHostDevice23AsyncDeviceRequest_ImplEP9IOServicehhtttP18IOMemoryDescriptorP8OSActionjE21kalloc_type_view_6014
+ __ZZN15IOUSBHostDevice36asyncDeviceRequestCompletionCallbackEPvS0_ijE21kalloc_type_view_5964
+ __ZZN16AppleUSBHostPort16terminateServiceEP9IOServiceE21kalloc_type_view_3159
+ __ZZN16AppleUSBHostPort16terminateServiceEP9IOServiceE21kalloc_type_view_3234
+ __ZZN16AppleUSBHostPort19cableChangeOccurredEP18IOTimerEventSourceE11_os_log_fmt_1
+ __ZZN16AppleUSBHostPort26terminateServiceThreadCallEPNS_30tPortTerminateServiceArgumentsEP11thread_callE21kalloc_type_view_3259
+ __ZZN21IOTypedOperatorsMixinI35AppleUSBHostControllerMapperSessionEdlEPvmE20kalloc_type_view_871
+ __ZZN21IOTypedOperatorsMixinI35AppleUSBHostControllerMapperSessionEnwEmE20kalloc_type_view_871
- __ZN16AppleUSBHostPort26terminateServiceThreadCallEP9IOServiceP11thread_call
- __ZZN15IOUSBHostDevice23AsyncDeviceRequest_ImplEP9IOServicehhtttP18IOMemoryDescriptorP8OSActionjE21kalloc_type_view_5978
- __ZZN15IOUSBHostDevice23AsyncDeviceRequest_ImplEP9IOServicehhtttP18IOMemoryDescriptorP8OSActionjE21kalloc_type_view_6009
- __ZZN15IOUSBHostDevice36asyncDeviceRequestCompletionCallbackEPvS0_ijE21kalloc_type_view_5959
CStrings:
+ "%s@%s: %s::%s: deferring power off\n"
+ "111"
+ "B16@?0^{OSSerialize=^^?i*III^{OSArray}^{OSArray}BB^v^v^{OSData}I}8"
+ "site.T"
+ "site.tPortTerminateServiceArguments"
- "B16@?0^{OSSerialize=^^?i*III^{OSArray}BB^v^v^{OSData}I}8"
```
