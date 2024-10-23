## libmecab.dylib

> `/usr/lib/libmecab.dylib`

```diff

-1092.3.105.0.0
-  __TEXT.__text: 0x49cf4
-  __TEXT.__auth_stubs: 0x720
-  __TEXT.__const: 0x1215
-  __TEXT.__cstring: 0x5451
-  __TEXT.__gcc_except_tab: 0x2e40
-  __TEXT.__unwind_info: 0xfa8
+1093.207.0.0.0
+  __TEXT.__text: 0x532d4
+  __TEXT.__auth_stubs: 0x730
+  __TEXT.__const: 0x163e
+  __TEXT.__cstring: 0x5716
+  __TEXT.__gcc_except_tab: 0x3090
+  __TEXT.__unwind_info: 0x10e8
   __DATA_CONST.__got: 0xd8
-  __DATA_CONST.__const: 0xbc0
-  __AUTH_CONST.__auth_got: 0x398
-  __AUTH_CONST.__auth_ptr: 0x68
-  __AUTH_CONST.__const: 0xb10
+  __DATA_CONST.__const: 0xb98
+  __AUTH_CONST.__auth_got: 0x3a0
+  __AUTH_CONST.__auth_ptr: 0x18
+  __AUTH_CONST.__const: 0x1108
+  __AUTH.__thread_vars: 0x18
+  __AUTH.__thread_bss: 0x100
   __DATA.__data: 0x2c
-  __DATA.__common: 0x13c
+  __DATA.__common: 0x3c
   __DATA.__bss: 0x18
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libiconv.2.dylib
-  Functions: 707
-  Symbols:   912
-  CStrings:  645
+  Functions: 876
+  Symbols:   1082
+  CStrings:  667
 
Symbols:
+ __tlv_bootstrap
+ _mecab_get_all_morphs
+ _mecab_get_partial
+ _mecab_get_theta
+ _mecab_lattice_add_request_type
+ _mecab_lattice_clear
+ _mecab_lattice_destroy
+ _mecab_lattice_get_all_begin_nodes
+ _mecab_lattice_get_all_end_nodes
+ _mecab_lattice_get_begin_nodes
+ _mecab_lattice_get_bos_node
+ _mecab_lattice_get_boundary_constraint
+ _mecab_lattice_get_end_nodes
+ _mecab_lattice_get_eos_node
+ _mecab_lattice_get_feature_constraint
+ _mecab_lattice_get_request_type
+ _mecab_lattice_get_sentence
+ _mecab_lattice_get_size
+ _mecab_lattice_get_theta
+ _mecab_lattice_get_z
+ _mecab_lattice_has_constraint
+ _mecab_lattice_has_request_type
+ _mecab_lattice_is_available
+ _mecab_lattice_nbest_tostr
+ _mecab_lattice_nbest_tostr2
+ _mecab_lattice_new
+ _mecab_lattice_new_node
+ _mecab_lattice_next
+ _mecab_lattice_remove_request_type
+ _mecab_lattice_set_boundary_constraint
+ _mecab_lattice_set_feature_constraint
+ _mecab_lattice_set_request_type
+ _mecab_lattice_set_result
+ _mecab_lattice_set_sentence
+ _mecab_lattice_set_sentence2
+ _mecab_lattice_set_theta
+ _mecab_lattice_set_z
+ _mecab_lattice_strerror
+ _mecab_lattice_tostr
+ _mecab_lattice_tostr2
+ _mecab_model_destroy
+ _mecab_model_dictionary_info
+ _mecab_model_lookup
+ _mecab_model_new
+ _mecab_model_new2
+ _mecab_model_new_lattice
+ _mecab_model_new_tagger
+ _mecab_model_swap
+ _mecab_model_transition_cost
+ _mecab_parse_lattice
+ _mecab_set_all_morphs
+ _mecab_set_partial
+ _mecab_set_theta
+ _sched_yield
CStrings:
+ " dictionary_charset="
+ " is not a binary model. reopen it as text mode..."
+ " is not found. skipped."
+ " may be broken: "
+ " model_charset="
+ "!model_charset.empty()"
+ "--cost --freq and --eta options are overwritten."
+ "0.00005"
+ "0.996"
+ "2 == tokenize2(const_cast<char *>(line.c_str()), \" \\t\", col, 2)"
+ "24"
+ "700"
+ "C: "
+ "Dictionary is empty"
+ "Invalid model is passed"
+ "MECAB_NBEST request type is not set"
+ "Model is not available"
+ "Passed model is not available"
+ "Transition table and dictionary are not compatible"
+ "Using previous model: "
+ "` doesn't allow an argument"
+ "` requires an argument"
+ "alpha_"
+ "assign-user-dictionary-costs"
+ "build model file"
+ "build system dictionary"
+ "build-charcategory"
+ "build-matrix"
+ "build-model"
+ "build-sysdic"
+ "build-unknown"
+ "cannot create model from="
+ "cannot create tagger"
+ "cannot open feature index"
+ "cannot open tokenizer"
+ "charset is empty"
+ "charset: "
+ "charset:             "
+ "cid.left_size() == matrix.left_size() && cid.right_size() == matrix.right_size()"
+ "connector_->open(param)"
+ "cost field should not be empty in sys/unk dic."
+ "current model is not available"
+ "d->open(dicfile[i])"
+ "d->type() == 1"
+ "decode_charset(charset_) == decode_charset(to.c_str())"
+ "decode_charset(model_charset.c_str()) == decode_charset(from.c_str())"
+ "dic_.empty()"
+ "dic_charset"
+ "dictionary charset and model charset are different. "
+ "dictionary_charset="
+ "don't validate pos ID values. (Apple specific)"
+ "eon-format"
+ "eta: "
+ "eval-size: "
+ "eval-size:           "
+ "feature.size() < buf.size() - 1"
+ "feature_index.save(model.c_str(), header.c_str())"
+ "features.size() == surfaces.size()"
+ "fi"
+ "fi->open(param)"
+ "freq: "
+ "header"
+ "iconv.convert(&feature)"
+ "iconv.open(model_charset.c_str(), dic_charset)"
+ "incompatible dictionary: "
+ "key_[n] == fp"
+ "lattice information level (DEPRECATED)"
+ "lattice-level is DEPERCATED. "
+ "left.size() > 0"
+ "len < buf.size() - 3"
+ "lpath is NULL"
+ "lpath->fvector"
+ "lsize == lines.size()"
+ "marginal"
+ "maxid_ == 0"
+ "maximum grouping size for unknown words (default 24)"
+ "model charset and dictionary charset are different. "
+ "model.bin"
+ "model.def"
+ "model_charset="
+ "n < col.size()"
+ "n.value != -1"
+ "nbest size must be 1 <= nbest <= 512"
+ "new_node->feature"
+ "no more results"
+ "no path information is available"
+ "node != nullptr"
+ "node is NULL"
+ "old-model"
+ "only assign costs/ids to user dictionary"
+ "openTextModel(param)"
+ "output marginal probability (default false)"
+ "partial parsing mode (default false)"
+ "property"
+ "property->open(param)"
+ "ret >= 0"
+ "rewriter"
+ "rewriter.rewrite(feature, &ufeature, &lfeature, &rfeature)"
+ "right.size() > 0"
+ "set DIR as dic dir (default \".\")"
+ "set FILE as old CRF model file"
+ "set cost factor (default 700)"
+ "std::strlen(feature) < buf.size() - 1"
+ "str.size() == len.size()"
+ "str.size() == val.size()"
+ "sysdic->isCompatible(*d)"
+ "sysdic->open (create_filename(prefix, SYS_DIC_FILE).c_str())"
+ "tokenize(buf.get(), \"\\t\", col, 2) == 2"
+ "tokenize2(buf.get(), \":\", column, 2) == 2"
+ "tokenize2(buf.get(), \"\\t \", column, 2) == 2"
+ "tokenize2(buf.get(), \"\\t \", column, 3) == 3"
+ "tokenize2(buf.get(), \"\\t\", column, 2) == 2"
+ "tokenizer.dictionary_info()"
+ "tokenizer_->dictionary_info()"
+ "tokenizer_->dictionary_info()->lsize == connector_->left_size() && tokenizer_->dictionary_info()->rsize == connector_->right_size()"
+ "tokenizer_->open(param)"
+ "type == MECAB_USR_DIC"
+ "unk-eval-size: "
+ "unk-eval-size:       "
+ "unkdic_.open(create_filename (prefix, UNK_DIC_FILE).c_str())"
+ "use --marginal or --nbest."
+ "use STR as the user-defined beginning-of-sentence format"
+ "use STR as the user-defined end-of-NBest format"
+ "use STR as the user-defined end-of-sentence format"
+ "use STR as the user-defined unknown node format"
+ "writer->writeNode(lattice.get(), node_format.c_str(), &node, &*os)"
- " default-emission-freq must be >= 0 "
- "!bos_feature.empty()"
- "(crf|hmm)"
- "*++p =='['"
- ".txt"
- "/Library/Caches/com.apple.xbs/Sources/Mecabra/src/viterbisub.h"
- "0.001"
- "0.5"
- "0.97"
- "0xffff != lsize"
- "2 == tokenize2(const_cast<char *>(line.c_str()), \" \\t\", std::back_inserter(col), 2)"
- "4000"
- "B"
- "B:%!r(MISSING)/%!l(MISSING)"
- "Done!"
- "U"
- "U:%!u(MISSING)"
- "` dosen't allow an argument"
- "` requres an argument"
- "bestNode"
- "build"
- "build binary model from text model"
- "charcategory"
- "connector_->open(*param)"
- "cost-factor is empty"
- "cost_factor_ > 0"
- "crf"
- "d->open(_dic[i], mode)"
- "d->type() == MECAB_USR_DIC"
- "da.build(key.size(), &key[0], 0, 0, 0) == 0"
- "default transition cost must be > 0"
- "default-emission-cost"
- "default-emission-freq"
- "default-transition-cost"
- "default-transition-freq"
- "default_emission_cost > 0"
- "default_transition_cost > 0"
- "don't validate pos ID values."
- "dump"
- "em-hmm"
- "feature.size() < sizeof(buf) - 1"
- "feature_index.convert(ifile.c_str(), model.c_str())"
- "feature_index.convert(txtfile.c_str(), model.c_str())"
- "feature_index.open(*param)"
- "feature_index.save(txtfile.c_str())"
- "format error\n"
- "format error in rewrite.def: "
- "freq >= 0.0"
- "identity-template"
- "lattice information level (default 0)"
- "left.size()"
- "len < sizeof(buf) - 3"
- "load_dictionary_resource(param)"
- "matrix"
- "n < psize"
- "n < sizeof(col)"
- "n.value != 0"
- "no path information, use -l option"
- "node != NULL"
- "node->feature[0] != '\\0'"
- "node->lpath"
- "open dictioanry with mutable mode (experimental)"
- "open-mutable-dictionary"
- "output text model only"
- "partial parsing mode"
- "ret > 0"
- "rewrite failed"
- "rewrite.rewrite(bos_feature, &ufeature, &plfeature, &prfeature)"
- "rewrite.rewrite(feature, &ufeature, &lfeature, &rfeature)"
- "right.size()"
- "set DIR as dicdi (default \".\")"
- "set default emission cost for HMM"
- "set default transition cost for HMM"
- "set the default emission frequency for HMM (default 0.5)"
- "set the default transition frequency for HMM (default 0.0)"
- "set training algorithm"
- "std::strcmp(\"B\", col[0]) == 0 && std::strcmp(\"U\", col[0]) == 0"
- "std::strlen(feature) < sizeof(buf) - 1"
- "sysdic"
- "sysdic->open(create_filename(prefix, SYS_DIC_FILE).c_str(), mode)"
- "text-only"
- "tokenize(buf, \"\\t\", std::back_inserter(col), 2) == 2"
- "tokenize(line, \"\\t\", std::back_inserter(col), 2) == 2"
- "tokenize(line, \"\\t\", std::back_inserter(col), 4) == 4"
- "tokenize2(buf, \"\\t\", std::back_inserter(column), 2) == 2"
- "tokenizeCSV(line, std::back_inserter(col), 5) == 5"
- "tokenizer_.open(*param)"
- "too long lines"
- "training-algorithm"
- "unkdic_->open(create_filename(prefix, UNK_DIC_FILE).c_str(), mode)"
- "unknown"
- "unknown error in building double array: "
- "unknown type: "
- "unkonwn meta char "
- "unkonwn meta char: "
- "use -l option to obtain N-Best results. e.g., mecab -N10 -l1"
- "use EM in HMM training (experimental)"
- "use STR as the user-defined bos format"
- "use STR as the user-defined eos format"
- "use STR as the user-defined unk format"
- "viterbi_.lattice_level() >= 1"
- "viterbi_.open(*param, &tokenizer_, connector_)"
- "writer->writeNode(&*os, node_format.c_str(), w.c_str(), &node)"
- "writer_.open(*param)"

```
