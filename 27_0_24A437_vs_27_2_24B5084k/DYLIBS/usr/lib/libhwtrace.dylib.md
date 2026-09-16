## libhwtrace.dylib

> `/usr/lib/libhwtrace.dylib`

```diff

-328.2.1.0.0
-  __TEXT.__text: 0x27b510
-  __TEXT.__const: 0x176f10
-  __TEXT.__cstring: 0x16f45
-  __TEXT.__oslogstring: 0xaa5
+328.40.29.0.0
+  __TEXT.__text: 0x27f264
+  __TEXT.__const: 0x176f40
+  __TEXT.__cstring: 0x17205
+  __TEXT.__oslogstring: 0xac5
   __TEXT.__gcc_except_tab: 0x390
-  __TEXT.__unwind_info: 0x4090
+  __TEXT.__unwind_info: 0x4108
   __TEXT.__eh_frame: 0xa0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 4867
-  Symbols:   597
-  CStrings:  4359
+  Functions: 4923
+  Symbols:   647
+  CStrings:  4376
 
Symbols:
+ _hwtrace_cluster_options_create
+ _hwtrace_cluster_options_destroy
+ _hwtrace_cursor_create_from_async_task
+ _hwtrace_cursor_create_from_core
+ _hwtrace_cursor_create_from_thread
+ _hwtrace_cursor_destroy
+ _hwtrace_cursor_previous_pc
+ _hwtrace_cursor_previous_range
+ _hwtrace_cursor_section
+ _hwtrace_isa_create
+ _hwtrace_isa_destroy
+ _hwtrace_live_recording_create_from_session
+ _hwtrace_live_recording_create_with_options
+ _hwtrace_live_recording_destroy
+ _hwtrace_live_recording_options_create
+ _hwtrace_live_recording_options_destroy
+ _hwtrace_live_recording_postprocess_options_create
+ _hwtrace_live_recording_postprocess_options_destroy
+ _hwtrace_live_recording_session_create
+ _hwtrace_live_recording_session_destroy
+ _hwtrace_load_options_create
+ _hwtrace_load_options_destroy
+ _hwtrace_range_cycle_count
+ _hwtrace_range_instruction_count
+ _hwtrace_recording_create_empty
+ _hwtrace_recording_create_from_corefile
+ _hwtrace_recording_create_from_directory
+ _hwtrace_recording_create_from_ktrace
+ _hwtrace_recording_create_from_live_recording
+ _hwtrace_recording_destroy
+ _hwtrace_recording_save_options_add_system
+ _hwtrace_recording_save_options_create
+ _hwtrace_recording_save_options_destroy
+ _hwtrace_section_disasm
+ _hwtrace_section_disassemble
+ _hwtrace_section_load_address
+ _hwtrace_section_module_name
+ _hwtrace_section_name
+ _hwtrace_section_offset_4CoreSymbolication
+ _hwtrace_section_segment_file_address
+ _hwtrace_section_segment_load_address
+ _hwtrace_section_segment_name
+ _hwtrace_section_slide
+ _hwtrace_section_symbol
+ _hwtrace_section_used_iter
+ _hwtrace_section_uuid
+ _hwtrace_task_sections_iter
+ _hwtrace_trace_create_from_directory
+ _hwtrace_trace_create_from_recording
+ _hwtrace_trace_destroy
CStrings:
+ " (requires H16G+)"
+ " + "
+ ", carveout="
+ ", fill="
+ ", size="
+ ". Available: "
+ "APT chunk fill_size exceeds size: fill_size="
+ "Address trace unsupported on "
+ "Chunk has no leading slice for wrap-no-copy mode: valid="
+ "Chunk slice out of bounds: "
+ "Chunk slice size too large: "
+ "ExceptionLevelFiltering.cpp"
+ "Failed to get SEP layout info. Make sure sepOS supports CPUTrace on this SoC."
+ "Failed to map the SEP carveout. Make sure the sep-cputrace-size boot-arg is set."
+ "Production trace cannot capture any of the requested exception levels: it always traces EL0, and the driver does not support tracing EL2"
+ "RTBuddy chunk pointers out of carveout: base="
+ "RTBuddy chunk translation failed"
+ "Save filter selects no systems"
+ "System containing this core was not loaded"
+ "Tracing EL0 alone is unsupported for development trace: enable production trace instead"
+ "Unknown system in save filter: "
+ "chunk{ base=%{public}llu, fill=%{public}llu, carveout_size=%{public}llu, wrap=%{public}u, loss=%{public}u }"
+ "hwtrace_isa_create"
+ "hwtrace_isa_destroy"
+ "libhwtrace @ tag libhwtrace-328.40.29"
+ "libhwtrace @ tag libhwtrace-328.40.29\n"
+ "tag libhwtrace-328.40.29"
- "Chunk offset out of bounds"
- "Chunk size out of bounds"
- "Chunk size too large"
- "IOConnectMapMemory LayoutInfo failed"
- "chunk{ chunk_id=%{public}llu, offset=%{public}llu, size=%{public}llu, fill_size=%{public}llu, fill_wrap=%{public}u }"
- "hwtrace_isa_deinit"
- "hwtrace_isa_init"
- "libhwtrace @ tag libhwtrace-328.2.1"
- "libhwtrace @ tag libhwtrace-328.2.1\n"
- "tag libhwtrace-328.2.1"
```
