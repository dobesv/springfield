from springfield import fields, Entity
from springfield.alias import Alias


class TestEntity(Entity):
    real = fields.StringField(doc='Actual, real field')
    fake = Alias('real')


def test_read_alias():
    t = TestEntity(real='fake')
    assert t.real == 'fake'
    assert t.fake == 'fake'

    
def test_write_alias():
    t = TestEntity(real='fake')
    t.fake = 'real'
    assert t.real == 'real'
    assert t.fake == 'real'
    

def test_init_alias():
    t = TestEntity(fake='real')
    assert t.real == 'real'
    assert t.fake == 'real'
    
    
def test_adapt_alias():
    t = TestEntity.adapt({'fake': 'real'})
    assert t.real == 'real'
    t = TestEntity.adapt({'real': 'fake'})
    assert t.fake == 'real'
