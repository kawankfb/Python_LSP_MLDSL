def test_1():
    from mldslls.dslf_language_helpers.semantic_token_full_provider import get_semantic_token_data
    result = get_semantic_token_data("D:\\input-1-refined.txt")
    return result


if __name__ == "__main__":
    print(test_1())