## libhwtrace.dylib

> `/usr/lib/libhwtrace.dylib`

```diff

-133.100.90.0.0
-  __TEXT.__text: 0x2202f0
-  __TEXT.__auth_stubs: 0x16a0
-  __TEXT.__const: 0x111250
-  __TEXT.__cstring: 0x18a05
-  __TEXT.__oslogstring: 0x99b
-  __TEXT.__gcc_except_tab: 0x37c
-  __TEXT.__unwind_info: 0x2920
-  __TEXT.__eh_frame: 0x48
-  __TEXT.__objc_classname: 0x1
-  __TEXT.__objc_methname: 0xa9
-  __TEXT.__objc_stubs: 0x120
-  __DATA_CONST.__got: 0x98
-  __DATA_CONST.__const: 0x45fd8
+306.0.0.0.0
+  __TEXT.__text: 0x2624d0
+  __TEXT.__const: 0x111c90
+  __TEXT.__cstring: 0x1da84
+  __TEXT.__oslogstring: 0xa1b
+  __TEXT.__gcc_except_tab: 0x390
+  __TEXT.__unwind_info: 0x3140
+  __TEXT.__eh_frame: 0x90
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_methname: 0x0
+  __DATA_CONST.__const: 0x46190
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x48
-  __AUTH_CONST.__auth_got: 0xb60
-  __AUTH_CONST.__const: 0x6230
-  __AUTH_CONST.__cfstring: 0x2e0
+  __DATA_CONST.__objc_selrefs: 0x50
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__const: 0x7468
+  __AUTH_CONST.__cfstring: 0x300
+  __AUTH_CONST.__weak_auth_got: 0x40
+  __AUTH_CONST.__auth_got: 0xb30
   __AUTH.__data: 0x18
-  __DATA.__data: 0x58
-  __DATA.__bss: 0xa30
+  __DATA.__data: 0x48
+  __DATA.__crash_info: 0x148
+  __DATA.__bss: 0xa78
   __DATA.__common: 0x170
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: E77ACD4C-08FC-3D1D-B92C-01F7949E4ACF
-  Functions: 4139
-  Symbols:   581
-  CStrings:  5412
+  UUID: 2A42C729-49FB-3432-BB42-F31FB79C4D7B
+  Functions: 4806
+  Symbols:   595
+  CStrings:  5570
 
Symbols:
+ _IORegistryEntryGetParentEntry
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE21__grow_by_and_replaceEmmmmmmPKc
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEPKc
+ __ZNSt3__132__internal_log_hardening_failureEPKc
+ __ZNSt3__16chrono12system_clock11from_time_tEl
+ _hwtrace_cluster_options_deinit
+ _hwtrace_cluster_options_init
+ _hwtrace_cluster_options_set_cluster_type
+ _hwtrace_cluster_options_set_core_count
+ _hwtrace_cluster_options_set_platform_generation
+ _hwtrace_cluster_set_raw_trace_path
+ _hwtrace_cursor_equals
+ _hwtrace_cursor_memory_accesses
+ _hwtrace_recording_add_system
+ _hwtrace_recording_init_empty
+ _hwtrace_recording_timebase_period
+ _hwtrace_system_add_cluster
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x8
- ___cxa_guard_abort
- _dyld_shared_cache_unpin_mapping
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
- _objc_retain_x20
CStrings:
+ "\n  The RTBuddy driver could not allocate the trace buffer.\n  Run the following commands then reboot:\n    `"
+ "\n=== HWTRACE_VERIFY_MEMACCESS Summary ===\n"
+ "    "
+ "    0x"
+ "    EL mismatch (GL1→GL2):  "
+ "    EL mismatch (any):      "
+ "    Fill seen, invalidated: "
+ "    No fill ever seen:      "
+ "    Stage "
+ "    broadcast (tid!=0): "
+ "    cmd "
+ "  --- EL mismatch breakdown (access EL -> fill EL: count) ---\n"
+ "  --- TLB fills by EL ---\n"
+ "  --- TLB fills by stage ---\n"
+ "  --- TLBI command histogram ---\n"
+ "  --- Untranslated breakdown ---\n"
+ "  Mismatched windows: "
+ "  Top encoding classes in mismatched windows:\n"
+ "  Total delta loads: "
+ "  Total delta stores: "
+ "  Total memory accesses:    "
+ "  Total sync windows checked: "
+ "  Translated:               "
+ "  Untranslated:             "
+ " (desynced)"
+ " -> "
+ " bytes): "
+ " bytes, have "
+ " consumed_stores="
+ " delta_ld="
+ " delta_st="
+ " is present but its filename is unknown: consider passing it in via the `apple-hwtrace record -image=...` argument. If using `trace record`, pass `--CPUTrace:sideload=path/to/your/image/override`."
+ " mismatch: consumed_loads="
+ " stores="
+ "'\n+ ["
+ "', got "
+ ", endTime="
+ ", expected "
+ ", expected: "
+ ".\n  Run the following command then reboot:\n    `"
+ "/AppleInternal/Library/BuildRoots/4~CQCiugBA2wftac8OYgolroNgUZDEaTI5FGh00KI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCiugBA2wftac8OYgolroNgUZDEaTI5FGh00KI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCiugBA2wftac8OYgolroNgUZDEaTI5FGh00KI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCiugBA2wftac8OYgolroNgUZDEaTI5FGh00KI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCiugBA2wftac8OYgolroNgUZDEaTI5FGh00KI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCiugBA2wftac8OYgolroNgUZDEaTI5FGh00KI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCiugBA2wftac8OYgolroNgUZDEaTI5FGh00KI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCiugBA2wftac8OYgolroNgUZDEaTI5FGh00KI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCiugBA2wftac8OYgolroNgUZDEaTI5FGh00KI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCiugBA2wftac8OYgolroNgUZDEaTI5FGh00KI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__bit_reference:113: libc++ Hardening assertion __ctz + __clz < sizeof(_StorageType) * 8 failed: __fill_masked_range called with invalid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCiugBA2wftac8OYgolroNgUZDEaTI5FGh00KI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__hash_table:1855: libc++ Hardening assertion __p != end() failed: unordered container::erase(iterator) called with a non-dereferenceable iterator\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCiugBA2wftac8OYgolroNgUZDEaTI5FGh00KI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__utility/is_pointer_in_range.h:38: libc++ Hardening assertion std::__is_valid_range(__begin, __end) failed: [__begin, __end) is not a valid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCiugBA2wftac8OYgolroNgUZDEaTI5FGh00KI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1156: libc++ Hardening assertion __first <= __last failed: vector::erase(first, last) called with invalid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCiugBA2wftac8OYgolroNgUZDEaTI5FGh00KI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__vector/vector.h:413: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCiugBA2wftac8OYgolroNgUZDEaTI5FGh00KI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__vector/vector.h:418: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCiugBA2wftac8OYgolroNgUZDEaTI5FGh00KI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: front() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCiugBA2wftac8OYgolroNgUZDEaTI5FGh00KI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__vector/vector.h:437: libc++ Hardening assertion !empty() failed: front() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCiugBA2wftac8OYgolroNgUZDEaTI5FGh00KI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__vector/vector.h:441: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCiugBA2wftac8OYgolroNgUZDEaTI5FGh00KI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__vector/vector.h:445: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCiugBA2wftac8OYgolroNgUZDEaTI5FGh00KI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__vector/vector.h:494: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCiugBA2wftac8OYgolroNgUZDEaTI5FGh00KI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/array:279: libc++ Hardening assertion __n < _Size failed: out-of-bounds access in std::array<T, N>\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCiugBA2wftac8OYgolroNgUZDEaTI5FGh00KI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/array:284: libc++ Hardening assertion __n < _Size failed: out-of-bounds access in std::array<T, N>\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCiugBA2wftac8OYgolroNgUZDEaTI5FGh00KI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/deque:1534: libc++ Hardening assertion __i < size() failed: deque::operator[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCiugBA2wftac8OYgolroNgUZDEaTI5FGh00KI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/deque:1565: libc++ Hardening assertion !empty() failed: deque::front called on an empty deque\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCiugBA2wftac8OYgolroNgUZDEaTI5FGh00KI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/deque:1577: libc++ Hardening assertion !empty() failed: deque::back called on an empty deque\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCiugBA2wftac8OYgolroNgUZDEaTI5FGh00KI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/deque:2199: libc++ Hardening assertion !empty() failed: deque::pop_front called on an empty deque\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCiugBA2wftac8OYgolroNgUZDEaTI5FGh00KI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/deque:2213: libc++ Hardening assertion !empty() failed: deque::pop_back called on an empty deque\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCiugBA2wftac8OYgolroNgUZDEaTI5FGh00KI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/optional:1112: libc++ Hardening assertion this->has_value() failed: optional operator-> called on a disengaged value\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCiugBA2wftac8OYgolroNgUZDEaTI5FGh00KI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/optional:1121: libc++ Hardening assertion this->has_value() failed: optional operator-> called on a disengaged value\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCiugBA2wftac8OYgolroNgUZDEaTI5FGh00KI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/optional:1130: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCiugBA2wftac8OYgolroNgUZDEaTI5FGh00KI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/optional:1139: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCiugBA2wftac8OYgolroNgUZDEaTI5FGh00KI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/optional:1148: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCiugBA2wftac8OYgolroNgUZDEaTI5FGh00KI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/string:1362: libc++ Hardening assertion __pos <= size() failed: string index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCiugBA2wftac8OYgolroNgUZDEaTI5FGh00KI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/string:1371: libc++ Hardening assertion __pos <= size() failed: string index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CQCiugBA2wftac8OYgolroNgUZDEaTI5FGh00KI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/string_view:331: libc++ Hardening assertion __len <= static_cast<size_type>(numeric_limits<difference_type>::max()) failed: string_view::string_view(_CharT *, size_t): length does not fit in difference_type\n"
+ "/System/Cryptexes/ExclaveOS/System/ExclaveKit"
+ "/System/Volumes/Preboot/Cryptexes/ExclaveOS/System/ExclaveKit"
+ ":                "
+ ":                  "
+ ": loads="
+ ": need "
+ "; full buffer ("
+ "=== Translation Diagnostics ===\n"
+ "========================================\n"
+ "?"
+ "AddressSpace::addSharedCacheSymbols"
+ "BaseAddrs.bin"
+ "Buffer too small for "
+ "Contextual"
+ "Counters.bin"
+ "Desynced"
+ "DivergedSplitState"
+ "EL"
+ "ElementLayout"
+ "ElementLayout missing or invalid ElementSize"
+ "ElementSize"
+ "EnergyCounts.bin"
+ "Error llvm::applehwtrace::RTBuddyDriverInterface::deinitLayoutInfo()"
+ "Error llvm::applehwtrace::RTBuddyDriverInterface::initLayoutInfo()"
+ "Expected exactly 1 cluster for system '"
+ "Expected<ScanTaskResult> llvm::applehwtrace::Monitor::scanTask(UniqueContext &)"
+ "FilesystemCache: caching item at %{public}s"
+ "FilesystemCache: removing stale item %{public}s"
+ "HWTRACE_VERIFY_MEMACCESS"
+ "IOConnectMapMemory LayoutInfo not available.\n  - Ensure firmware is calling RTK_tracekit_transport_log_system_layout at boot\n  - Ensure supports_cputrace: True is set in the pitayaOS device-tree\n  - Run the following command then reboot:\n    `"
+ "IOConnectUnmapMemory LayoutInfo failed"
+ "IODeviceTree"
+ "IODeviceTree:/arm-io"
+ "InsecureContextID"
+ "LastContextID"
+ "LayoutInfo total_size exceeds buffer"
+ "MemAccesses.bin"
+ "MsgHdr"
+ "No r-x segments for UUID "
+ "PC"
+ "PendingSWMsgHeader"
+ "Prescan"
+ "Prescan: invalid unit"
+ "Prescan: trace loss"
+ "PrescanDiagnostic"
+ "PrevPCUpdate"
+ "Prod trace EL2 unsupported on "
+ "RTBuddy layout info not available for "
+ "RTBuddyARG"
+ "RTBuddyV3"
+ "Redirects.bin"
+ "SWMsgUnitIndex"
+ "SecureContextID"
+ "SplitBeforeNextInst"
+ "SyncDiagnostic"
+ "SyncResult"
+ "TLBI_ALLE1"
+ "TLBI_ALLE2"
+ "TLBI_ALLE3"
+ "TLBI_ASIDE1"
+ "TLBI_IPAS2E1"
+ "TLBI_IPAS2LE1"
+ "TLBI_RIPAS2E1"
+ "TLBI_RIPAS2LE1"
+ "TLBI_RVAAE1"
+ "TLBI_RVAALE1"
+ "TLBI_RVAE1"
+ "TLBI_RVAE2"
+ "TLBI_RVAE3"
+ "TLBI_RVALE1"
+ "TLBI_RVALE2"
+ "TLBI_RVALE3"
+ "TLBI_UNKNOWN"
+ "TLBI_VAAE1"
+ "TLBI_VAALE1"
+ "TLBI_VAE1"
+ "TLBI_VAE2"
+ "TLBI_VAE3"
+ "TLBI_VALE1"
+ "TLBI_VALE2"
+ "TLBI_VALE3"
+ "TLBI_VMALLE1"
+ "TLBI_VMALLS12E1"
+ "TemplateRanges"
+ "TemplateRanges.bin"
+ "This commonly happens when a trace buffer is not allocated. Run the following commands then reboot:\n    `"
+ "TraceStopped"
+ "Translations.bin"
+ "UnitIndex"
+ "Unsupported CPUTRACE_METADATA_MAJOR_VERSION: got "
+ "Unsupported RTBUDDY_TRACE_LAYOUT_VERSION got: "
+ "VERIFY_MEMACCESS: sync window "
+ "VM region already mapped.\n["
+ "_SPTMRuntimeExceptionVectorBase"
+ "__direct_entry"
+ "__endpoint_entry"
+ "__start"
+ "_rtb_cputrace_carveout_mb=<buffer-size-in-mb>"
+ "_sptm_entry_handler"
+ "`"
+ "`\n    `"
+ "` in your `apple-hwtrace record ...` invocation to fix this. If using `trace record`, pass `--CPUTrace:sideload=path/to/your/image/override`."
+ "asid"
+ "auto llvm::applehwtrace::RTBuddyDriverInterface::get(StringRef)::(anonymous class)::operator()(io_service_t) const"
+ "bootargs remove phys_carveout_mb"
+ "bootargs set "
+ "bootargs set apt_carveout_mb=256"
+ "bootargs set panic_trace=0x4"
+ "cluster type is required"
+ "cmd"
+ "compatible"
+ "csw"
+ "el"
+ "fresh"
+ "generation is required"
+ "json-manifest-indent"
+ "libhwtrace @ tag libhwtrace-306"
+ "libhwtrace @ tag libhwtrace-306\n"
+ "mpidr"
+ "nG"
+ "num"
+ "orig"
+ "pa"
+ "ppn"
+ "prev-tid"
+ "rtbuddy_trace_address_space_t"
+ "rtbuddy_trace_image_t"
+ "rtbuddy_trace_layout_t"
+ "scale"
+ "shared cache has no files"
+ "sizepow2"
+ "stage"
+ "subsumed by fixup"
+ "super-ranges"
+ "tg"
+ "tid"
+ "time"
+ "va"
+ "visitLoadCommands: not an understood Mach header."
+ "vmid"
+ "vpn"
- " is present but its filename is unknown: consider passing it in via the `apple-hwtrace record -image=...` argument. If using `trace record`, see 111873589 for a workaround."
- "\" and \""
- "' for "
- "+ ["
- "ASC8_CHINOOK_TCORE"
- "ASC8_TEMPEST_ECORE"
- "Compression"
- "Could not create child iterator for RTBuddy("
- "Could not create matching dictionary for RTBuddy"
- "Could not find IOService(s) matching RTBuddy"
- "Error llvm::applehwtrace::Monitor::getThreadIDs(UniqueContext &, task_read_t, const SystemTrace::LockToken &)"
- "Error llvm::applehwtrace::Monitor::scanTask(UniqueContext &, const SystemTrace::LockToken &)"
- "InDyldSharedCache"
- "Multiple r-x segments in image "
- "No r-x segments in image "
- "Not supported"
- "Single-process filtering enabled: expected exactly 1 task context, but got "
- "This commonly happens when a trace buffer is not allocated. Try running the following commands: `"
- "Timestamps"
- "URLForDirectory:inDomain:appropriateForURL:create:error:"
- "UTF8String"
- "Unsupported CPUTRACE_METADATA_MAJOR_VERSION"
- "Unsupported minor format version"
- "VM region already mapped."
- "_"
- "_C"
- "__TEXT"
- "_dyld_framework_HWTrace_spis_enabled"
- "` in your `apple-hwtrace record ...` invocation to fix this. If using `trace record`, see 111873589 for a workaround."
- "` then rebooting."
- "ane"
- "ane0"
- "ane1"
- "ave"
- "ave0"
- "ave1"
- "ave2"
- "ave3"
- "boolForKey:"
- "bootargs remove phys_carveout_mb; bootargs set apt_carveout_mb=256"
- "branch island overlap"
- "cannot open tmpfile at "
- "cluster-"
- "core-"
- "defaultManager"
- "dyld4hwtrace"
- "initWithSuiteName:"
- "isp"
- "isp0"
- "libhwtrace @ tag libhwtrace-133.100.90"
- "libhwtrace @ tag libhwtrace-133.100.90\n"
- "nXS"
- "objectForKey:"
- "path"
- "static Expected<std::unique_ptr<RTBuddyDriverInterface>> llvm::applehwtrace::RTBuddyDriverInterface::get(StringRef)"
- "stringForKey:"
- "stringWithUTF8String:"
- "task_threads failed"
- "thread_info failed"

```
