## Hypervisor

> `/System/Library/Frameworks/Hypervisor.framework/Versions/A/Hypervisor`

```diff

-205.0.0.0.0
-  __TEXT.__text: 0x61320
+206.0.0.0.0
+  __TEXT.__text: 0x6113c
   __TEXT.__auth_stubs: 0x6b0
-  __TEXT.__const: 0x1a9a
-  __TEXT.__gcc_except_tab: 0x2110
+  __TEXT.__const: 0x1aca
+  __TEXT.__gcc_except_tab: 0x2104
   __TEXT.__cstring: 0x1b69
   __TEXT.__oslogstring: 0x3
-  __TEXT.__unwind_info: 0x1540
+  __TEXT.__unwind_info: 0x1388
   __TEXT.__objc_classname: 0x5a
   __DATA_CONST.__got: 0x90
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __AUTH_CONST.__auth_got: 0x360
   __AUTH_CONST.__auth_ptr: 0x10
-  __AUTH_CONST.__const: 0x35f0
+  __AUTH_CONST.__const: 0x3570
   __AUTH_CONST.__objc_const: 0x2d0
   __AUTH.__objc_data: 0x190
   __AUTH.__thread_vars: 0x18

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1954
-  Symbols:   2544
+  Functions: 1944
+  Symbols:   2528
   CStrings:  494
 
Symbols:
+ GCC_except_table106
+ GCC_except_table1418
+ GCC_except_table1426
+ GCC_except_table1439
+ GCC_except_table1443
+ GCC_except_table1444
+ GCC_except_table1445
+ GCC_except_table1446
+ GCC_except_table1447
+ GCC_except_table1448
+ GCC_except_table1483
+ GCC_except_table1485
+ GCC_except_table1504
+ GCC_except_table1505
+ GCC_except_table1506
+ GCC_except_table1509
+ GCC_except_table1513
+ GCC_except_table1516
+ GCC_except_table22
+ GCC_except_table42
+ GCC_except_table42
+ GCC_except_table56
+ GCC_except_table58
+ GCC_except_table60
+ GCC_except_table62
+ GCC_except_table65
+ GCC_except_table68
+ GCC_except_table70
+ GCC_except_table72
+ GCC_except_table74
+ GCC_except_table76
+ GCC_except_table88
+ GCC_except_table90
+ __ZN2Hv2Vm16map_nested_spaceERKN6HvCore10Hypervisor27GuestHypervisorSpaceManager5SpaceEPvymyy
+ __ZN2Hv2Vm18reset_nested_spaceERN6HvCore20NestedGuestMemoryMap12AddressSpaceE
+ __ZN2Hv2Vm18unmap_nested_spaceERKN6HvCore10Hypervisor27GuestHypervisorSpaceManager5SpaceEym
+ __ZN2Hv4Vcpu16map_nested_spaceERKN6HvCore10Hypervisor27GuestHypervisorSpaceManager5SpaceEPvyymN4Base9OptionSetINS8_10ProtectionEEE
+ __ZN2Hv4Vcpu18unmap_nested_spaceERKN6HvCore10Hypervisor27GuestHypervisorSpaceManager5SpaceEym
+ __ZN2Hv4Vcpu24mark_user_requested_exitEv
+ __ZN3Arm11CpuFeatures40round_down_to_valid_pa_range_field_valueEj
+ __ZN6HvCore10Hypervisor27GuestHypervisorSpaceManager16purge_space_implERNS1_9SpaceImplENS1_9SpaceTypeE
+ __ZN6HvCore10Hypervisor27GuestHypervisorSpaceManager25for_each_mapping_in_rangeERKNS1_5SpaceENS_20NestedGuestMemoryMap18AddressSpaceActionEN3Arm27IntermediatePhysicalAddressEmRKNSt3__18functionIFbRKNS5_11MappedRangeEEEE
+ __ZN6HvCore10Hypervisor27GuestHypervisorSpaceManager36remove_each_physical_address_mappingENS_15PhysicalAddressEmRKNSt3__18functionIFbyRKNS_20NestedGuestMemoryMap11MappedRangeEEEE
+ __ZN6HvCore10Hypervisor27GuestHypervisorSpaceManager37protect_each_physical_address_mappingENS_15PhysicalAddressEmN4Base9OptionSetINS3_10ProtectionEEERKNSt3__18functionIFbyRKNS_20NestedGuestMemoryMap11MappedRangeEEEE
+ __ZN6HvCore10Hypervisor27GuestHypervisorSpaceManager3mapERKNS1_5SpaceEN3Arm27IntermediatePhysicalAddressENS_15PhysicalAddressEmPvN4Base9OptionSetINS9_10ProtectionEEERKNSt3__18functionIFbNS_20NestedGuestMemoryMap9RangeInfoERKNSF_11MappedRangeEEEE
+ __ZN6HvCore10Hypervisor27GuestHypervisorSpaceManager6createERNS1_8DelegateEjhh
+ __ZN6HvCore10Hypervisor27GuestHypervisorSpaceManagerD2Ev
+ __ZN6HvCore20NestedGuestMemoryMap19reset_address_spaceEy
+ __ZNKSt3__110__function6__funcIZN2Hv2Vm16map_nested_spaceERKN6HvCore10Hypervisor27GuestHypervisorSpaceManager5SpaceEPvymyyE3$_0NS_9allocatorISB_EEFbNS4_20NestedGuestMemoryMap9RangeInfoERKNSE_11MappedRangeEEE11target_typeEv
+ __ZNKSt3__110__function6__funcIZN2Hv2Vm16map_nested_spaceERKN6HvCore10Hypervisor27GuestHypervisorSpaceManager5SpaceEPvymyyE3$_0NS_9allocatorISB_EEFbNS4_20NestedGuestMemoryMap9RangeInfoERKNSE_11MappedRangeEEE6targetERKSt9type_info
+ __ZNKSt3__110__function6__funcIZN2Hv2Vm16map_nested_spaceERKN6HvCore10Hypervisor27GuestHypervisorSpaceManager5SpaceEPvymyyE3$_0NS_9allocatorISB_EEFbNS4_20NestedGuestMemoryMap9RangeInfoERKNSE_11MappedRangeEEE7__cloneEPNS0_6__baseISJ_EE
+ __ZNKSt3__110__function6__funcIZN2Hv2Vm16map_nested_spaceERKN6HvCore10Hypervisor27GuestHypervisorSpaceManager5SpaceEPvymyyE3$_0NS_9allocatorISB_EEFbNS4_20NestedGuestMemoryMap9RangeInfoERKNSE_11MappedRangeEEE7__cloneEv
+ __ZNKSt3__110__function6__funcIZN2Hv2Vm18unmap_nested_spaceERKN6HvCore10Hypervisor27GuestHypervisorSpaceManager5SpaceEymE3$_0NS_9allocatorISA_EEFbRKNS4_20NestedGuestMemoryMap11MappedRangeEEE11target_typeEv
+ __ZNKSt3__110__function6__funcIZN2Hv2Vm18unmap_nested_spaceERKN6HvCore10Hypervisor27GuestHypervisorSpaceManager5SpaceEymE3$_0NS_9allocatorISA_EEFbRKNS4_20NestedGuestMemoryMap11MappedRangeEEE6targetERKSt9type_info
+ __ZNKSt3__110__function6__funcIZN2Hv2Vm18unmap_nested_spaceERKN6HvCore10Hypervisor27GuestHypervisorSpaceManager5SpaceEymE3$_0NS_9allocatorISA_EEFbRKNS4_20NestedGuestMemoryMap11MappedRangeEEE7__cloneEPNS0_6__baseISH_EE
+ __ZNKSt3__110__function6__funcIZN2Hv2Vm18unmap_nested_spaceERKN6HvCore10Hypervisor27GuestHypervisorSpaceManager5SpaceEymE3$_0NS_9allocatorISA_EEFbRKNS4_20NestedGuestMemoryMap11MappedRangeEEE7__cloneEv
+ __ZNSt3__110__function6__funcIZN2Hv2Vm16map_nested_spaceERKN6HvCore10Hypervisor27GuestHypervisorSpaceManager5SpaceEPvymyyE3$_0NS_9allocatorISB_EEFbNS4_20NestedGuestMemoryMap9RangeInfoERKNSE_11MappedRangeEEE18destroy_deallocateEv
+ __ZNSt3__110__function6__funcIZN2Hv2Vm16map_nested_spaceERKN6HvCore10Hypervisor27GuestHypervisorSpaceManager5SpaceEPvymyyE3$_0NS_9allocatorISB_EEFbNS4_20NestedGuestMemoryMap9RangeInfoERKNSE_11MappedRangeEEE7destroyEv
+ __ZNSt3__110__function6__funcIZN2Hv2Vm16map_nested_spaceERKN6HvCore10Hypervisor27GuestHypervisorSpaceManager5SpaceEPvymyyE3$_0NS_9allocatorISB_EEFbNS4_20NestedGuestMemoryMap9RangeInfoERKNSE_11MappedRangeEEED0Ev
+ __ZNSt3__110__function6__funcIZN2Hv2Vm16map_nested_spaceERKN6HvCore10Hypervisor27GuestHypervisorSpaceManager5SpaceEPvymyyE3$_0NS_9allocatorISB_EEFbNS4_20NestedGuestMemoryMap9RangeInfoERKNSE_11MappedRangeEEED1Ev
+ __ZNSt3__110__function6__funcIZN2Hv2Vm16map_nested_spaceERKN6HvCore10Hypervisor27GuestHypervisorSpaceManager5SpaceEPvymyyE3$_0NS_9allocatorISB_EEFbNS4_20NestedGuestMemoryMap9RangeInfoERKNSE_11MappedRangeEEEclEOSF_SI_
+ __ZNSt3__110__function6__funcIZN2Hv2Vm18unmap_nested_spaceERKN6HvCore10Hypervisor27GuestHypervisorSpaceManager5SpaceEymE3$_0NS_9allocatorISA_EEFbRKNS4_20NestedGuestMemoryMap11MappedRangeEEE18destroy_deallocateEv
+ __ZNSt3__110__function6__funcIZN2Hv2Vm18unmap_nested_spaceERKN6HvCore10Hypervisor27GuestHypervisorSpaceManager5SpaceEymE3$_0NS_9allocatorISA_EEFbRKNS4_20NestedGuestMemoryMap11MappedRangeEEE7destroyEv
+ __ZNSt3__110__function6__funcIZN2Hv2Vm18unmap_nested_spaceERKN6HvCore10Hypervisor27GuestHypervisorSpaceManager5SpaceEymE3$_0NS_9allocatorISA_EEFbRKNS4_20NestedGuestMemoryMap11MappedRangeEEED0Ev
+ __ZNSt3__110__function6__funcIZN2Hv2Vm18unmap_nested_spaceERKN6HvCore10Hypervisor27GuestHypervisorSpaceManager5SpaceEymE3$_0NS_9allocatorISA_EEFbRKNS4_20NestedGuestMemoryMap11MappedRangeEEED1Ev
+ __ZNSt3__110__function6__funcIZN2Hv2Vm18unmap_nested_spaceERKN6HvCore10Hypervisor27GuestHypervisorSpaceManager5SpaceEymE3$_0NS_9allocatorISA_EEFbRKNS4_20NestedGuestMemoryMap11MappedRangeEEEclESG_
+ __ZTINSt3__110__function6__funcIZN2Hv2Vm16map_nested_spaceERKN6HvCore10Hypervisor27GuestHypervisorSpaceManager5SpaceEPvymyyE3$_0NS_9allocatorISB_EEFbNS4_20NestedGuestMemoryMap9RangeInfoERKNSE_11MappedRangeEEEE
+ __ZTINSt3__110__function6__funcIZN2Hv2Vm18unmap_nested_spaceERKN6HvCore10Hypervisor27GuestHypervisorSpaceManager5SpaceEymE3$_0NS_9allocatorISA_EEFbRKNS4_20NestedGuestMemoryMap11MappedRangeEEEE
+ __ZTIZN2Hv2Vm16map_nested_spaceERKN6HvCore10Hypervisor27GuestHypervisorSpaceManager5SpaceEPvymyyE3$_0
+ __ZTIZN2Hv2Vm18unmap_nested_spaceERKN6HvCore10Hypervisor27GuestHypervisorSpaceManager5SpaceEymE3$_0
+ __ZTSNSt3__110__function6__funcIZN2Hv2Vm16map_nested_spaceERKN6HvCore10Hypervisor27GuestHypervisorSpaceManager5SpaceEPvymyyE3$_0NS_9allocatorISB_EEFbNS4_20NestedGuestMemoryMap9RangeInfoERKNSE_11MappedRangeEEEE
+ __ZTSNSt3__110__function6__funcIZN2Hv2Vm18unmap_nested_spaceERKN6HvCore10Hypervisor27GuestHypervisorSpaceManager5SpaceEymE3$_0NS_9allocatorISA_EEFbRKNS4_20NestedGuestMemoryMap11MappedRangeEEEE
+ __ZTSZN2Hv2Vm16map_nested_spaceERKN6HvCore10Hypervisor27GuestHypervisorSpaceManager5SpaceEPvymyyE3$_0
+ __ZTSZN2Hv2Vm18unmap_nested_spaceERKN6HvCore10Hypervisor27GuestHypervisorSpaceManager5SpaceEymE3$_0
+ __ZTVNSt3__110__function6__funcIZN2Hv2Vm16map_nested_spaceERKN6HvCore10Hypervisor27GuestHypervisorSpaceManager5SpaceEPvymyyE3$_0NS_9allocatorISB_EEFbNS4_20NestedGuestMemoryMap9RangeInfoERKNSE_11MappedRangeEEEE
+ __ZTVNSt3__110__function6__funcIZN2Hv2Vm18unmap_nested_spaceERKN6HvCore10Hypervisor27GuestHypervisorSpaceManager5SpaceEymE3$_0NS_9allocatorISA_EEFbRKNS4_20NestedGuestMemoryMap11MappedRangeEEEE
+ __ZThn8_N2Hv4Vcpu16map_nested_spaceERKN6HvCore10Hypervisor27GuestHypervisorSpaceManager5SpaceEPvyymN4Base9OptionSetINS8_10ProtectionEEE
+ __ZThn8_N2Hv4Vcpu18unmap_nested_spaceERKN6HvCore10Hypervisor27GuestHypervisorSpaceManager5SpaceEym
- GCC_except_table116
- GCC_except_table1417
- GCC_except_table1420
- GCC_except_table1436
- GCC_except_table1438
- GCC_except_table1442
- GCC_except_table1475
- GCC_except_table1477
- GCC_except_table1479
- GCC_except_table1494
- GCC_except_table1495
- GCC_except_table1498
- GCC_except_table1502
- GCC_except_table1503
- GCC_except_table1511
- GCC_except_table1517
- GCC_except_table1520
- GCC_except_table1521
- GCC_except_table23
- GCC_except_table32
- GCC_except_table41
- GCC_except_table43
- GCC_except_table53
- GCC_except_table59
- GCC_except_table61
- GCC_except_table64
- GCC_except_table66
- GCC_except_table66
- GCC_except_table69
- GCC_except_table71
- GCC_except_table73
- GCC_except_table75
- GCC_except_table81
- GCC_except_table89
- __ZN2Hv2Vm16map_nested_spaceEyPvymyy
- __ZN2Hv2Vm18reset_nested_spaceEy
- __ZN2Hv2Vm18unmap_nested_spaceEyym
- __ZN2Hv4Vcpu16map_nested_spaceEyPvyymN4Base9OptionSetINS2_10ProtectionEEE
- __ZN2Hv4Vcpu18unmap_nested_spaceEyym
- __ZN6HvCore10Hypervisor27GuestHypervisorSpaceManager29try_get_space_matching_lockedEN3Arm8VttbrEl2ENS1_16BaseAddressCheckE
- __ZN6HvCore10Hypervisor27GuestHypervisorSpaceManager6createERNS1_8DelegateEjj
- __ZN6HvCore20NestedGuestMemoryMap16for_each_mappingEyNS0_18AddressSpaceActionERKNSt3__18functionIFbRKNS0_11MappedRangeEEEE
- __ZN6HvCore20NestedGuestMemoryMap25for_each_mapping_in_rangeEyNS0_18AddressSpaceActionEN3Arm27IntermediatePhysicalAddressEmRKNSt3__18functionIFbRKNS0_11MappedRangeEEEE
- __ZN6HvCore20NestedGuestMemoryMap36remove_each_physical_address_mappingENS_15PhysicalAddressEmRKNSt3__18functionIFbyRKNS0_11MappedRangeEEEE
- __ZN6HvCore20NestedGuestMemoryMap37protect_each_physical_address_mappingENS_15PhysicalAddressEmN4Base9OptionSetINS2_10ProtectionEEERKNSt3__18functionIFbyRKNS0_11MappedRangeEEEE
- __ZN6HvCore20NestedGuestMemoryMap3mapEyN3Arm27IntermediatePhysicalAddressENS_15PhysicalAddressEmPvN4Base9OptionSetINS5_10ProtectionEEERKNSt3__18functionIFbNS0_9RangeInfoERKNS0_11MappedRangeEEEE
- __ZN6HvCore20NestedGuestMemoryMap5purgeEy
- __ZN6HvCore20NestedGuestMemoryMapC1Ehj
- __ZNKSt3__110__function6__funcIZN2Hv2Vm16map_nested_spaceEyPvymyyE3$_0NS_9allocatorIS5_EEFbN6HvCore20NestedGuestMemoryMap9RangeInfoERKNS9_11MappedRangeEEE11target_typeEv
- __ZNKSt3__110__function6__funcIZN2Hv2Vm16map_nested_spaceEyPvymyyE3$_0NS_9allocatorIS5_EEFbN6HvCore20NestedGuestMemoryMap9RangeInfoERKNS9_11MappedRangeEEE6targetERKSt9type_info
- __ZNKSt3__110__function6__funcIZN2Hv2Vm16map_nested_spaceEyPvymyyE3$_0NS_9allocatorIS5_EEFbN6HvCore20NestedGuestMemoryMap9RangeInfoERKNS9_11MappedRangeEEE7__cloneEPNS0_6__baseISE_EE
- __ZNKSt3__110__function6__funcIZN2Hv2Vm16map_nested_spaceEyPvymyyE3$_0NS_9allocatorIS5_EEFbN6HvCore20NestedGuestMemoryMap9RangeInfoERKNS9_11MappedRangeEEE7__cloneEv
- __ZNKSt3__110__function6__funcIZN2Hv2Vm18reset_nested_spaceEyE3$_0NS_9allocatorIS4_EEFbRKN6HvCore20NestedGuestMemoryMap11MappedRangeEEE11target_typeEv
- __ZNKSt3__110__function6__funcIZN2Hv2Vm18reset_nested_spaceEyE3$_0NS_9allocatorIS4_EEFbRKN6HvCore20NestedGuestMemoryMap11MappedRangeEEE6targetERKSt9type_info
- __ZNKSt3__110__function6__funcIZN2Hv2Vm18reset_nested_spaceEyE3$_0NS_9allocatorIS4_EEFbRKN6HvCore20NestedGuestMemoryMap11MappedRangeEEE7__cloneEPNS0_6__baseISC_EE
- __ZNKSt3__110__function6__funcIZN2Hv2Vm18reset_nested_spaceEyE3$_0NS_9allocatorIS4_EEFbRKN6HvCore20NestedGuestMemoryMap11MappedRangeEEE7__cloneEv
- __ZNKSt3__110__function6__funcIZN2Hv2Vm18unmap_nested_spaceEyymE3$_0NS_9allocatorIS4_EEFbRKN6HvCore20NestedGuestMemoryMap11MappedRangeEEE11target_typeEv
- __ZNKSt3__110__function6__funcIZN2Hv2Vm18unmap_nested_spaceEyymE3$_0NS_9allocatorIS4_EEFbRKN6HvCore20NestedGuestMemoryMap11MappedRangeEEE6targetERKSt9type_info
- __ZNKSt3__110__function6__funcIZN2Hv2Vm18unmap_nested_spaceEyymE3$_0NS_9allocatorIS4_EEFbRKN6HvCore20NestedGuestMemoryMap11MappedRangeEEE7__cloneEPNS0_6__baseISC_EE
- __ZNKSt3__110__function6__funcIZN2Hv2Vm18unmap_nested_spaceEyymE3$_0NS_9allocatorIS4_EEFbRKN6HvCore20NestedGuestMemoryMap11MappedRangeEEE7__cloneEv
- __ZNKSt3__114default_deleteIN6HvCore10Hypervisor27GuestHypervisorSpaceManagerEEclB8fe180100EPS3_
- __ZNSt3__110__function6__funcIZN2Hv2Vm16map_nested_spaceEyPvymyyE3$_0NS_9allocatorIS5_EEFbN6HvCore20NestedGuestMemoryMap9RangeInfoERKNS9_11MappedRangeEEE18destroy_deallocateEv
- __ZNSt3__110__function6__funcIZN2Hv2Vm16map_nested_spaceEyPvymyyE3$_0NS_9allocatorIS5_EEFbN6HvCore20NestedGuestMemoryMap9RangeInfoERKNS9_11MappedRangeEEE7destroyEv
- __ZNSt3__110__function6__funcIZN2Hv2Vm16map_nested_spaceEyPvymyyE3$_0NS_9allocatorIS5_EEFbN6HvCore20NestedGuestMemoryMap9RangeInfoERKNS9_11MappedRangeEEED0Ev
- __ZNSt3__110__function6__funcIZN2Hv2Vm16map_nested_spaceEyPvymyyE3$_0NS_9allocatorIS5_EEFbN6HvCore20NestedGuestMemoryMap9RangeInfoERKNS9_11MappedRangeEEED1Ev
- __ZNSt3__110__function6__funcIZN2Hv2Vm16map_nested_spaceEyPvymyyE3$_0NS_9allocatorIS5_EEFbN6HvCore20NestedGuestMemoryMap9RangeInfoERKNS9_11MappedRangeEEEclEOSA_SD_
- __ZNSt3__110__function6__funcIZN2Hv2Vm18reset_nested_spaceEyE3$_0NS_9allocatorIS4_EEFbRKN6HvCore20NestedGuestMemoryMap11MappedRangeEEE18destroy_deallocateEv
- __ZNSt3__110__function6__funcIZN2Hv2Vm18reset_nested_spaceEyE3$_0NS_9allocatorIS4_EEFbRKN6HvCore20NestedGuestMemoryMap11MappedRangeEEE7destroyEv
- __ZNSt3__110__function6__funcIZN2Hv2Vm18reset_nested_spaceEyE3$_0NS_9allocatorIS4_EEFbRKN6HvCore20NestedGuestMemoryMap11MappedRangeEEED0Ev
- __ZNSt3__110__function6__funcIZN2Hv2Vm18reset_nested_spaceEyE3$_0NS_9allocatorIS4_EEFbRKN6HvCore20NestedGuestMemoryMap11MappedRangeEEED1Ev
- __ZNSt3__110__function6__funcIZN2Hv2Vm18reset_nested_spaceEyE3$_0NS_9allocatorIS4_EEFbRKN6HvCore20NestedGuestMemoryMap11MappedRangeEEEclESB_
- __ZNSt3__110__function6__funcIZN2Hv2Vm18unmap_nested_spaceEyymE3$_0NS_9allocatorIS4_EEFbRKN6HvCore20NestedGuestMemoryMap11MappedRangeEEE18destroy_deallocateEv
- __ZNSt3__110__function6__funcIZN2Hv2Vm18unmap_nested_spaceEyymE3$_0NS_9allocatorIS4_EEFbRKN6HvCore20NestedGuestMemoryMap11MappedRangeEEE7destroyEv
- __ZNSt3__110__function6__funcIZN2Hv2Vm18unmap_nested_spaceEyymE3$_0NS_9allocatorIS4_EEFbRKN6HvCore20NestedGuestMemoryMap11MappedRangeEEED0Ev
- __ZNSt3__110__function6__funcIZN2Hv2Vm18unmap_nested_spaceEyymE3$_0NS_9allocatorIS4_EEFbRKN6HvCore20NestedGuestMemoryMap11MappedRangeEEED1Ev
- __ZNSt3__110__function6__funcIZN2Hv2Vm18unmap_nested_spaceEyymE3$_0NS_9allocatorIS4_EEFbRKN6HvCore20NestedGuestMemoryMap11MappedRangeEEEclESB_
- __ZNSt3__110unique_ptrIN6HvCore20NestedGuestMemoryMapENS_14default_deleteIS2_EEED1B8fe180100Ev
- __ZTINSt3__110__function6__funcIZN2Hv2Vm16map_nested_spaceEyPvymyyE3$_0NS_9allocatorIS5_EEFbN6HvCore20NestedGuestMemoryMap9RangeInfoERKNS9_11MappedRangeEEEE
- __ZTINSt3__110__function6__funcIZN2Hv2Vm18reset_nested_spaceEyE3$_0NS_9allocatorIS4_EEFbRKN6HvCore20NestedGuestMemoryMap11MappedRangeEEEE
- __ZTINSt3__110__function6__funcIZN2Hv2Vm18unmap_nested_spaceEyymE3$_0NS_9allocatorIS4_EEFbRKN6HvCore20NestedGuestMemoryMap11MappedRangeEEEE
- __ZTIZN2Hv2Vm16map_nested_spaceEyPvymyyE3$_0
- __ZTIZN2Hv2Vm18reset_nested_spaceEyE3$_0
- __ZTIZN2Hv2Vm18unmap_nested_spaceEyymE3$_0
- __ZTSNSt3__110__function6__funcIZN2Hv2Vm16map_nested_spaceEyPvymyyE3$_0NS_9allocatorIS5_EEFbN6HvCore20NestedGuestMemoryMap9RangeInfoERKNS9_11MappedRangeEEEE
- __ZTSNSt3__110__function6__funcIZN2Hv2Vm18reset_nested_spaceEyE3$_0NS_9allocatorIS4_EEFbRKN6HvCore20NestedGuestMemoryMap11MappedRangeEEEE
- __ZTSNSt3__110__function6__funcIZN2Hv2Vm18unmap_nested_spaceEyymE3$_0NS_9allocatorIS4_EEFbRKN6HvCore20NestedGuestMemoryMap11MappedRangeEEEE
- __ZTSZN2Hv2Vm16map_nested_spaceEyPvymyyE3$_0
- __ZTSZN2Hv2Vm18reset_nested_spaceEyE3$_0
- __ZTSZN2Hv2Vm18unmap_nested_spaceEyymE3$_0
- __ZTVNSt3__110__function6__funcIZN2Hv2Vm16map_nested_spaceEyPvymyyE3$_0NS_9allocatorIS5_EEFbN6HvCore20NestedGuestMemoryMap9RangeInfoERKNS9_11MappedRangeEEEE
- __ZTVNSt3__110__function6__funcIZN2Hv2Vm18reset_nested_spaceEyE3$_0NS_9allocatorIS4_EEFbRKN6HvCore20NestedGuestMemoryMap11MappedRangeEEEE
- __ZTVNSt3__110__function6__funcIZN2Hv2Vm18unmap_nested_spaceEyymE3$_0NS_9allocatorIS4_EEFbRKN6HvCore20NestedGuestMemoryMap11MappedRangeEEEE
- __ZThn8_N2Hv4Vcpu16map_nested_spaceEyPvyymN4Base9OptionSetINS2_10ProtectionEEE
- __ZThn8_N2Hv4Vcpu18unmap_nested_spaceEyym

```
