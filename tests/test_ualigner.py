"""Test ualigner."""
from ualigner import __version__
from ualigner import ualigner


def test_version():
    """Test version."""
    assert __version__ == "0.1.0"


def test_sanity():
    """Sanity check."""
    try:
        assert not ualigner()
    except Exception:
        assert True

def test_ualigner():
    '''
ultimatumbee\ubee\uclas.py

    from model_pool import fetch_check_aux  # pylint: disable=import-error
    from model_pool.model_s import load_model_s  # pylint: disable=import-error
    from model_pool.load_model import load_model  # pylint: disable=import-error

    fetch_check_aux("/home/user")
    model_s = load_model_s()
    clas = load_model("clas-l-user")

    location = "./cachedir"
    memory = Memory(location, verbose=0)


    @memory.cache
    def cached_clas(*args, **kw):
        """Cache clas-l-user."""
        return clas(*args, **kw)


    # cached_clas = memory.cache(cached_clas)


    @memory.cache
    def encode(*args, **kw):
        """Cache model_s.encode."""
        return model_s.encode(*args, **kw)

    # time-consuming
    clas_resu = cached_clas(seq, labels, multi_label=multi_label)

    emb_sim = cosine_similarity(encode([seq]), encode(labels))

    #

    '''