## liblzma.5.dylib

> `/usr/lib/liblzma.5.dylib`

```diff

-18.0.0.0.0
-  __TEXT.__text: 0x1207c
-  __TEXT.__auth_stubs: 0x90
-  __TEXT.__const: 0x6448
-  __TEXT.__cstring: 0x6
-  __TEXT.__unwind_info: 0x3a4
+20.0.0.0.0
+  __TEXT.__text: 0x17c2c
+  __TEXT.__auth_stubs: 0x1d0
+  __TEXT.__const: 0x6498
+  __TEXT.__cstring: 0x310
+  __TEXT.__unwind_info: 0x4a0
   __DATA_CONST.__got: 0x8
-  __AUTH_CONST.__auth_got: 0x48
+  __DATA_CONST.__const: 0xd8
+  __AUTH_CONST.__const: 0x1e0
+  __AUTH_CONST.__auth_got: 0xe8
   __DATA.__data: 0x8
-  __DATA_DIRTY.__const: 0x318
+  __DATA_DIRTY.__const: 0x3c8
   - /usr/lib/libSystem.B.dylib
-  Functions: 282
-  Symbols:   474
-  CStrings:  1
+  Functions: 361
+  Symbols:   635
+  CStrings:  34
 
Symbols:
+ _CC_SHA256_Final
+ _CC_SHA256_Init
+ _CC_SHA256_Update
+ _arm64_code
+ _bcj_optmap
+ _block_buffer_encode
+ _clock_gettime
+ _delta_optmap
+ _file_info_decode
+ _file_info_decoder_end
+ _file_info_decoder_memconfig
+ _filter_name_map
+ _get_options
+ _get_progress
+ _get_thread
+ _lz_encoder_set_out_limit
+ _lzip_decode
+ _lzip_decoder_end
+ _lzip_decoder_get_check
+ _lzip_decoder_memconfig
+ _lzma12_mf_map
+ _lzma12_mode_map
+ _lzma12_optmap
+ _lzma_alloc_zero
+ _lzma_block_buffer_bound64
+ _lzma_block_uncomp_encode
+ _lzma_cputhreads
+ _lzma_file_info_decoder
+ _lzma_file_info_decoder_init
+ _lzma_filters_free
+ _lzma_get_progress
+ _lzma_index_decoder_init
+ _lzma_lzip_decoder
+ _lzma_lzip_decoder_init
+ _lzma_lzma2_block_size
+ _lzma_lzma_preset.depths
+ _lzma_lzma_preset.dict_pow2
+ _lzma_lzma_set_out_limit
+ _lzma_microlzma_decoder
+ _lzma_microlzma_encoder
+ _lzma_mt_block_size
+ _lzma_outq_clear_cache
+ _lzma_outq_clear_cache2
+ _lzma_outq_enable_partial_output
+ _lzma_outq_end
+ _lzma_outq_get_buf
+ _lzma_outq_init
+ _lzma_outq_is_readable
+ _lzma_outq_memusage
+ _lzma_outq_prealloc_buf
+ _lzma_outq_read
+ _lzma_simple_arm64_decoder_init
+ _lzma_simple_arm64_encoder_init
+ _lzma_str_from_filters
+ _lzma_str_list_filters
+ _lzma_str_to_filters
+ _lzma_stream_decoder_mt
+ _lzma_stream_encoder_mt
+ _lzma_stream_encoder_mt_memusage
+ _lzma_validate_chain
+ _malloc_type_calloc
+ _memchr
+ _microlzma_decode
+ _microlzma_decoder_end
+ _microlzma_decoder_init
+ _microlzma_encode
+ _microlzma_encoder_end
+ _microlzma_encoder_init
+ _move_head_to_cache
+ _parse_bcj
+ _parse_delta
+ _parse_lzma12
+ _parse_options
+ _pthread_cond_destroy
+ _pthread_cond_init
+ _pthread_cond_signal
+ _pthread_cond_timedwait
+ _pthread_cond_wait
+ _pthread_create
+ _pthread_join
+ _pthread_mutex_destroy
+ _pthread_mutex_init
+ _pthread_mutex_lock
+ _pthread_mutex_unlock
+ _pthread_sigmask
+ _read_output_and_wait
+ _reverse_seek
+ _str_append_str
+ _str_append_u32
+ _str_append_u32.suffixes
+ _stream_decode_mt
+ _stream_decoder_mt_end
+ _stream_decoder_mt_get_check
+ _stream_decoder_mt_get_progress
+ _stream_decoder_mt_init
+ _stream_decoder_mt_memconfig
+ _stream_encode_mt
+ _stream_encoder_init
+ _stream_encoder_mt_end
+ _stream_encoder_mt_init
+ _stream_encoder_mt_update
+ _strlen
+ _sysconf
+ _threads_end
+ _threads_stop
+ _tuklib_cpucores
+ _worker_decoder
+ _worker_enable_partial_update
+ _worker_error
+ _worker_start
- _SHA256_K
- _free_properties
- _index_decoder_init
- _lzma_lz_decoder_uncompressed
- _lzma_sha256_finish
- _lzma_sha256_init
- _lzma_sha256_init.s
- _lzma_sha256_update
- _lzma_stream_encoder_init
- _process
- _validate_chain
CStrings:
+ "\n"
+ " "
+ ","
+ "-"
+ "--"
+ "0"
+ "0-9[e]"
+ "5.4.3"
+ ":"
+ "="
+ "=<"
+ ">"
+ "Empty string is not allowed, try \"6\" if a default value is needed"
+ "Filter name is missing"
+ "Invalid filter chain ('lzma2' missing at the end?)"
+ "Invalid multiplier suffix (KiB, MiB, or GiB)"
+ "Invalid option value"
+ "Memory allocation failed"
+ "Option value cannot be empty"
+ "Options must be 'name=value' pairs separated with commas"
+ "The maximum number of filters is four"
+ "The sum of lc and lp must not exceed 4"
+ "This filter cannot be used in the .xz format"
+ "This option does not support any integer suffixes"
+ "UNKNOWN"
+ "Unexpected NULL pointer argument(s) to lzma_str_to_filters()"
+ "Unknown filter name"
+ "Unknown option name"
+ "Unsupported flags to lzma_str_to_filters()"
+ "Unsupported preset"
+ "Unsupported preset flag"
+ "Value is not a non-negative decimal integer"
+ "Value out of range"
+ "|"
- "5.0.5"

```
