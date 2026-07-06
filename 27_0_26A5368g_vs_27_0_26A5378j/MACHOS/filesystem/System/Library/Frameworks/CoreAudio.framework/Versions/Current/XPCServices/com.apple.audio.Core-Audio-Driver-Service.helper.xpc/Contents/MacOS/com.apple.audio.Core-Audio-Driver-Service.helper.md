## com.apple.audio.Core-Audio-Driver-Service.helper

> `/System/Library/Frameworks/CoreAudio.framework/Versions/Current/XPCServices/com.apple.audio.Core-Audio-Driver-Service.helper.xpc/Contents/MacOS/com.apple.audio.Core-Audio-Driver-Service.helper`

```diff

-  __TEXT.__text: 0x1d114
+  __TEXT.__text: 0x1cd60
   __TEXT.__realtime: 0x74
   __TEXT.__auth_stubs: 0xbd0
   __TEXT.__objc_stubs: 0xc00
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __TEXT.__cstring : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_selrefs : content changed
~ __DATA.__data : content changed
Functions:
~ __ZNSt3__117__call_once_proxyB9nqe220106INS_5tupleIJOZN4AMCP13Feature_FlagsL24access_event_link_oop_ioEPKbE3$_0EEEEEvPv : 716 -> 692
~ __ZNSt3__117__call_once_proxyB9nqe220106INS_5tupleIJOZN4AMCP13Feature_FlagsL26access_collect_io_perfdataEPKbE3$_0EEEEEvPv : 716 -> 692
~ __ZNSt3__134__uninitialized_allocator_relocateB9nqe220106INS_9allocatorINS_4pairIjNS_13unordered_mapIj21Custom_Property_TypesNS_4hashIjEENS_8equal_toIjEENS1_INS2_IKjS4_EEEEEEEEEEPSD_EEvRT_T0_SI_SI_ : 140 -> 124
~ -[Core_Audio_Driver store_change_info:for_token:] : 1004 -> 1000
~ -[Core_Audio_Driver initialize:reply:] : 584 -> 572
~ ___77-[Core_Audio_Driver perform_device_configuration_change:action:change:reply:]_block_invoke : 640 -> 628
~ ___75-[Core_Audio_Driver abort_device_configuration_change:action:change:reply:]_block_invoke : 640 -> 628
~ -[Core_Audio_Driver create_and_start_io_receiver:client_id:nominal_sample_rate:io_buffer_frame_size:work_group_port:io_messenger:] : 7420 -> 7364
~ -[Core_Audio_Driver add_device_client:client_id:process_id:is_native_endianess:bundle_id:reply:] : 484 -> 472
~ -[Core_Audio_Driver remove_device_client:client_id:process_id:is_native_endianess:bundle_id:reply:] : 484 -> 472
~ -[Core_Audio_Driver create_device:client_id:process_id:is_native_endianess:bundle_id:reply:] : 524 -> 512
~ -[Core_Audio_Driver destroy_device:reply:] : 424 -> 412
~ -[Core_Audio_Driver object_was_destroyed:reply:] : 996 -> 984
~ -[Core_Audio_Driver handle_register_buffer:] : 940 -> 928
~ -[Core_Audio_Driver handle_unregister_buffer:] : 2540 -> 2516
~ -[Core_Audio_Driver start_io:client_id:reply:] : 472 -> 460
~ -[Core_Audio_Driver start_synchronous_messenger:client_id:nominal_sample_rate:io_buffer_frame_size:work_group_port:io_messenger:reply:] : 532 -> 520
~ -[Core_Audio_Driver stop_synchronous_messenger:client_id:reply:] : 624 -> 612
~ -[Core_Audio_Driver has_property:reply:] : 408 -> 396
~ -[Core_Audio_Driver is_property_settable:reply:] : 424 -> 412
~ -[Core_Audio_Driver get_property_data_size:qualifier:reply:] : 688 -> 676
~ __ZL26unpack_data_from_qualifierN4AMCP3HAL22HAL_Property_Type_CodeEP6NSData : 928 -> 924
~ -[Core_Audio_Driver get_property_data:qualifier:data_size:reply:] : 2068 -> 2056
~ -[Core_Audio_Driver set_property_data:qualifier:data:reply:] : 2492 -> 2456
~ __ZN4AMCP7Utility22With_Realtime_DisabledC2Ev : 2180 -> 2152
~ __ZN4AMCP7Utility22With_Realtime_DisabledD2Ev : 884 -> 872
~ __Z17get_asp_interfaceN10applesauce2CF6URLRefE : 3848 -> 3796
~ ___74-[Core_Audio_Driver_Host_Proxy driver_properties_changed:properties_data:]_block_invoke : 444 -> 432
~ ___57-[Core_Audio_Driver_Host_Proxy copy_from_driver_storage:]_block_invoke : 436 -> 424
~ ___70-[Core_Audio_Driver_Host_Proxy write_to_driver_storage:property_list:]_block_invoke : 436 -> 424
~ ___59-[Core_Audio_Driver_Host_Proxy delete_from_driver_storage:]_block_invoke : 436 -> 424
~ -[Core_Audio_Driver_Host_Proxy driver_request_config_change:change_action:change_info:] : 940 -> 928
~ ___87-[Core_Audio_Driver_Host_Proxy driver_request_config_change:change_action:change_info:]_block_invoke : 444 -> 432
~ -[Core_Audio_Driver_Service get_driver_name_list:reply:] : 1760 -> 1736
~ -[Core_Audio_Driver_Service load_driver:driver_name:reply:] : 5180 -> 5096
~ __ZL20apply_resource_usageN10applesauce2CF9StringRefERKNS0_13DictionaryRefE : 1800 -> 1776
~ -[Core_Audio_Driver_Service load_deferred_driver:bundle_id:info:] : 5540 -> 5408
~ ___65-[Core_Audio_Driver_Service load_deferred_driver:bundle_id:info:]_block_invoke : 1044 -> 1008
~ -[Core_Audio_Driver_Service exit_service] : 252 -> 240
~ __ZN4AMCP6Portal3IPC11IO_Receiver15register_bufferEPU24objcproto13OS_xpc_object8NSObject : 2604 -> 2600
~ __ZNSt3__110__function6__funcIZN4AMCP6Portal3IPC11IO_Receiver20start_message_threadEvE3$_0FvRN5caulk3ipc13mapped_memoryEEEclESA_ : 1996 -> 1960
~ __ZN5caulk12thread_proxyINSt3__15tupleIJNS_6thread10attributesEZN4AMCP6Portal3IPC11IO_Receiver20start_message_threadEvE3$_1NS2_IJEEEEEEEEPvSC_ : 3996 -> 3944
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UUmNaE/Sources/AudioHAL/MCP/AMCP/API/Configuration.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UUmNaE/Sources/AudioHAL/MCP/AMCP/Utility/Thread_Utilities.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UUmNaE/Sources/AudioHAL/Source/Core_Audio_Driver_Service/Core_Audio_Driver_Service.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UUmNaE/Sources/AudioHAL/Source/HAL/Core/Portal/Audio_Server_PlugIn_Utilities.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UUmNaE/Sources/AudioHAL/Source/HAL/Core/Portal/Driver/Core_Audio_Driver.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UUmNaE/Sources/AudioHAL/Source/HAL/Core/Portal/Driver/Core_Audio_Driver_Host_Proxy.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UUmNaE/Sources/AudioHAL/Source/HAL/Core/Portal/Driver/IO_Receiver.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hwLYKQ/Sources/AudioHAL/MCP/AMCP/API/Configuration.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hwLYKQ/Sources/AudioHAL/MCP/AMCP/Utility/Thread_Utilities.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hwLYKQ/Sources/AudioHAL/Source/Core_Audio_Driver_Service/Core_Audio_Driver_Service.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hwLYKQ/Sources/AudioHAL/Source/HAL/Core/Portal/Audio_Server_PlugIn_Utilities.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hwLYKQ/Sources/AudioHAL/Source/HAL/Core/Portal/Driver/Core_Audio_Driver.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hwLYKQ/Sources/AudioHAL/Source/HAL/Core/Portal/Driver/Core_Audio_Driver_Host_Proxy.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hwLYKQ/Sources/AudioHAL/Source/HAL/Core/Portal/Driver/IO_Receiver.mm"

```
